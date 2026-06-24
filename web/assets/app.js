// Stocks Wiki — vanilla terminal shell (clock, theme, search, command bar, domain filter).
(function(){
  var app=document.getElementById('app');
  // live UTC clock
  var clk=document.getElementById('clock');
  function tick(){var d=new Date();clk&&(clk.textContent=d.toISOString().slice(11,19));}
  tick();setInterval(tick,1000);
  // theme toggle
  var tt=document.getElementById('theme-toggle');
  tt&&tt.addEventListener('click',function(){
    var h=document.documentElement,d=h.getAttribute('data-theme')==='dark'?'light':'dark';
    h.setAttribute('data-theme',d);document.getElementById('theme-label').textContent=d.toUpperCase();
    try{localStorage.setItem('sw-theme',d);}catch(e){}
  });
  try{var st=localStorage.getItem('sw-theme');if(st){document.documentElement.setAttribute('data-theme',st);var l=document.getElementById('theme-label');l&&(l.textContent=st.toUpperCase());}}catch(e){}
  // collapsible sidebar folders (VS-Code style) — header toggles its item list
  document.querySelectorAll('.nav-grp .hd').forEach(function(h){
    h.addEventListener('click',function(){h.parentNode.classList.toggle('open');});
  });
  // domain filter (dim non-matching nav items)
  var chips=document.getElementById('domain-chips');
  chips&&chips.addEventListener('click',function(e){
    var b=e.target.closest('.chip');if(!b)return;
    chips.querySelectorAll('.chip').forEach(function(c){c.classList.remove('on');});b.classList.add('on');
    var d=b.getAttribute('data-domain');
    document.querySelectorAll('.nav-i').forEach(function(n){
      n.classList.toggle('dim', d!=='all' && n.getAttribute('data-domain')!==d);
    });
  });
  // screener — sortable columns (% out / days-cover)
  var scr=document.getElementById('screener');
  if(scr){
    scr.querySelectorAll('th.sortable').forEach(function(th){
      th.addEventListener('click',function(){
        var k=th.getAttribute('data-k'),asc=th.classList.contains('on')&&!th.classList.contains('asc');
        scr.querySelectorAll('th').forEach(function(o){o.classList.remove('on','asc');});
        th.classList.add('on');if(asc)th.classList.add('asc');
        var tb=scr.tBodies[0],rows=[].slice.call(tb.rows);
        rows.sort(function(a,b){var x=+a.getAttribute('data-'+k),y=+b.getAttribute('data-'+k);return asc?x-y:y-x;});
        rows.forEach(function(r){tb.appendChild(r);});
      });
    });
  }
  // structure — segmented view switch (board / map / graph)
  var stabs=document.getElementById('struct-tabs');
  if(stabs){
    stabs.addEventListener('click',function(e){
      var b=e.target.closest('button');if(!b)return;
      stabs.querySelectorAll('button').forEach(function(x){x.classList.remove('on');});b.classList.add('on');
      var v=b.getAttribute('data-v');
      document.querySelectorAll('.struct-view').forEach(function(sv){
        sv.classList.toggle('hide', sv.getAttribute('data-view')!==v);
      });
      if(v==='graph')drawGraph();
    });
  }
  // structure — SVG connection graph (concentric rings: center + ring1 + ring2)
  var graphDrawn=false;
  function drawGraph(){
    if(graphDrawn)return; var el=document.getElementById('cgraph');
    var data=document.getElementById('graph-data'); if(!el||!data)return;
    var g; try{g=JSON.parse(data.textContent);}catch(e){return;}
    graphDrawn=true;
    var W=900,H=560,cx=W/2,cy=H/2,R1=160,R2=250;
    var pos={}, byRing={0:[],1:[],2:[]};
    g.nodes.forEach(function(n){byRing[n.ring].push(n);});
    pos[g.center]={x:cx,y:cy};
    function place(arr,rad){arr.forEach(function(n,i){
      var a=(-Math.PI/2)+(2*Math.PI*i/arr.length);
      pos[n.id]={x:cx+rad*Math.cos(a),y:cy+rad*Math.sin(a)};});}
    place(byRing[1],R1); place(byRing[2],R2);
    var NS='http://www.w3.org/2000/svg', svg='';
    // edges first (under nodes)
    g.edges.forEach(function(e){
      var p=pos[e.a],q=pos[e.b]; if(!p||!q)return;
      svg+='<line x1="'+p.x.toFixed(1)+'" y1="'+p.y.toFixed(1)+'" x2="'+q.x.toFixed(1)+'" y2="'+q.y.toFixed(1)+'" class="gedge"/>';
    });
    // nodes
    g.nodes.forEach(function(n){
      var p=pos[n.id]; if(!p)return;
      var r=Math.max(7,Math.min(26,7+n.deg*0.9));
      var fs=n.ring===0?13:10.5;
      svg+='<g class="gnode" data-out="'+n.out+'">'
        +'<circle cx="'+p.x.toFixed(1)+'" cy="'+p.y.toFixed(1)+'" r="'+r.toFixed(1)+'" fill="'+n.hex+'" fill-opacity="'+(n.ring===0?'.95':'.8')+'" stroke="'+n.hex+'"/>'
        +'<text x="'+p.x.toFixed(1)+'" y="'+(p.y+r+11).toFixed(1)+'" text-anchor="middle" font-size="'+fs+'" fill="var(--text-2)">'+n.label+'</text>'
        +'</g>';
    });
    el.innerHTML=svg;
    el.querySelectorAll('.gnode').forEach(function(gn){
      gn.addEventListener('click',function(){var o=gn.getAttribute('data-out');if(o)location.href=rel()+o;});
    });
  }
  if(stabs && location.hash==='#graph'){ // deep-link support (command bar "graph")
    var gb=stabs.querySelector('[data-v="graph"]'); gb&&gb.click();
  } else if(stabs && location.hash==='#map'){
    var mb=stabs.querySelector('[data-v="map"]'); mb&&mb.click();
  }
  // forward-edge — segmented domain filter
  var fef=document.getElementById('fe-filter');
  if(fef){
    fef.addEventListener('click',function(e){
      var b=e.target.closest('button');if(!b)return;
      fef.querySelectorAll('button').forEach(function(x){x.classList.remove('on');});b.classList.add('on');
      var f=b.getAttribute('data-f');
      document.querySelectorAll('.fe-card').forEach(function(c){
        c.classList.toggle('hide', f!=='all' && c.getAttribute('data-domain')!==f);
      });
    });
  }
  // search index
  var IDX=[];
  fetch(window.SEARCH_URL).then(function(r){return r.json();}).then(function(j){IDX=j;}).catch(function(){});
  function match(q){q=q.toLowerCase().trim();if(!q)return[];
    return IDX.filter(function(p){return p.title.toLowerCase().indexOf(q)>=0||(p.tickers||[]).some(function(t){return t.toLowerCase().indexOf(q)>=0;});}).slice(0,7);}
  var si=document.getElementById('search'),sr=document.getElementById('search-results');
  si&&si.addEventListener('input',function(){
    var m=match(si.value);
    if(!si.value.trim()){sr.classList.remove('open');return;}
    sr.innerHTML=m.length?m.map(function(p){return '<a href="'+rel()+p.out+'"><span class="tag">'+p.type+'</span>'+p.title+'</a>';}).join(''):'<a><span class="tag">—</span>No matches.</a>';
    sr.classList.add('open');
  });
  document.addEventListener('click',function(e){if(sr&&!e.target.closest('.sb-search'))sr.classList.remove('open');});
  function rel(){var s=window.SEARCH_URL||'';return s.replace(/search-index\.json$/,'');}
  // command bar
  var cmd=document.getElementById('cmd'),go=document.getElementById('go');
  function route(){
    var s=(cmd.value||'').toLowerCase().trim();if(!s)return;var r=rel();
    if(/graph|network|connection/.test(s))return nav(r+'structure.html#graph');
    if(/\bmap\b|layer/.test(s))return nav(r+'structure.html#map');
    if(/board|leader|choke|struct|analy/.test(s))return nav(r+'structure.html');
    var m=match(s)[0]||IDX.filter(function(p){return (p.tickers||[]).some(function(t){return t.toLowerCase()===s;});})[0];
    nav(m?r+m.out:r+'index.html');
  }
  function nav(u){location.href=u;}
  go&&go.addEventListener('click',route);
  cmd&&cmd.addEventListener('keydown',function(e){if(e.key==='Enter')route();});
  // "/" focuses search
  document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement!==si&&document.activeElement!==cmd){e.preventDefault();si&&si.focus();}});
})();
