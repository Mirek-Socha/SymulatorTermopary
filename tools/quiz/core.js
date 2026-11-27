/* ── QUIZ — pytania sprawdzające (wspólny moduł) ─────────────── */
const Quiz=(()=>{
  let order=[],perm=[],i=0,score=0,answered=false,picked=-1;
  const $=id=>document.getElementById(id);
  const shuffle=a=>{a=a.slice();for(let k=a.length-1;k>0;k--){const j=Math.floor(Math.random()*(k+1));[a[k],a[j]]=[a[j],a[k]];}return a;};
  function start(){order=shuffle(QUIZ_Q.map((_,k)=>k));i=0;score=0;answered=false;newPerm();}
  function newPerm(){const q=QUIZ_Q[order[i]];perm=q?shuffle(q.opts.map((_,k)=>k)):[];picked=-1;}
  function open(){if(!order.length)start();$('qzBack').style.display='none';$('quizOv').classList.add('open');render();}
  function close(){$('quizOv').classList.remove('open');}
  function render(){
    const body=$('qzBody'), n=QUIZ_Q.length;
    if(i>=n){
      const pct=Math.round(score/n*100);
      const msg=pct>=90?'Świetnie — materiał opanowany.':pct>=70?'Dobrze — przejrzyj wyjaśnienia pytań z błędami.':pct>=50?'Połowicznie — wróć do zakładki 📖 Teoria i spróbuj ponownie.':'Warto jeszcze raz przejść przez Teorię i poeksperymentować z symulatorem.';
      $('qzProg').textContent=`${n}/${n}`;
      body.innerHTML=`<div class="qz-sum"><div class="qz-score">${score} / ${n}</div><div class="qz-pct">${pct} %</div><p>${msg}</p>
        <button class="qz-btn qz-pri" onclick="Quiz.restart()">↻ Od nowa (nowa kolejność)</button></div>`;
      return;
    }
    const q=QUIZ_Q[order[i]];
    $('qzProg').textContent=`${i+1}/${n} · wynik ${score}`;
    const opts=perm.map((k,pos)=>{
      let cls='qz-opt';
      if(answered){ if(k===q.a) cls+=' ok'; else if(pos===picked) cls+=' bad'; else cls+=' dim'; }
      return `<button class="${cls}" ${answered?'disabled':''} onclick="Quiz.answer(${pos})"><span class="qz-l">${'ABCD'[pos]}</span>${q.opts[k]}</button>`;
    }).join('');
    const fb=answered?`<div class="qz-fb ${perm[picked]===q.a?'ok':'bad'}"><b>${perm[picked]===q.a?'✓ Dobrze.':'✗ Niestety nie.'}</b> ${q.exp}</div>`:'';
    body.innerHTML=`<div class="qz-topic">${q.topic}</div><p class="qz-q">${q.q}</p><div class="qz-opts">${opts}</div>${fb}
      <div class="qz-nav">${q.setup?`<button class="qz-btn" onclick="Quiz.tryIt()" title="Ustawia scenariusz pytania w symulatorze">🔬 Sprawdź w symulatorze</button>`:''}
      <button class="qz-btn qz-pri" ${answered?'':'disabled'} onclick="Quiz.next()">${i+1<n?'Dalej →':'Wynik'}</button></div>`;
  }
  function answer(pos){if(answered)return;answered=true;picked=pos;if(perm[pos]===QUIZ_Q[order[i]].a)score++;render();}
  function next(){i++;answered=false;if(i<QUIZ_Q.length)newPerm();render();}
  function tryIt(){const q=QUIZ_Q[order[i]];if(q&&q.setup)q.setup();close();$('qzBack').style.display='block';}
  function restart(){start();render();}
  return {open,close,answer,next,tryIt,restart};
})();
