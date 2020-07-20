const GetSum_Math = ( a, b ) => {

  return ((Math.max(a-b) + 1)*(a + b)) / 2 
};
console.log(GetSum_Math(0,-1))

// const GetSum_Recursive = ( a, b ) => {
//   if ( a === b ) return (a);
//   if ( a > b ) return ( a + GetSum_Recursive(a-1,b));
//   if ( a < b ) return ( a + GetSum_Recursive(a+1,a));
// };

// function getSum_First( a,b )
// {
//   var sum = 0;

//   if ( a > b ) {
//     a += b;
//     b = a-b;
//     a -= b;
//   }
//   for( i=a; i <= b; i++ ) {
//     sum += i;
//   }
//   return sum;
// }
