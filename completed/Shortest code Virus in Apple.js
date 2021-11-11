sc=(a,n)=>{
  for(;n-->0;)
    a=a.map((l,x)=>l.map((c,y)=>
      [[1,0],[-1,0],[0,1],[0,-1]].some(([i,j])=>a[x+i]&&a[x+i][y+j]=='V')?'V':c))
  return a}