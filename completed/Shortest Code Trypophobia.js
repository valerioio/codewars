sc=a=>{
  f={};
  m=0;
  a.forEach(b=>{b.forEach(n=>{
    f[n]=f[n]?f[n]+1:1;
    m=m>f[n]?m:f[n];})
  });
  return a.map(b=>b.filter(n=>f[n]!=m));
}