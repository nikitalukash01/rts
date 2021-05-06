function Facto(number) {
  if (number < 0) return {};

  if (!(number % 2)) return { x: number / 2, y: 2 };

  let num1, num2;
  let num = Math.ceil(Math.sqrt(number));
  for (let k = 0; k >= 0; k++) {
     num1 = num + k;
    let del = Math.pow(num1, 2) - number;
    if (del < 0) continue;
    let del1 = Math.sqrt(del);
    if (Number.isInteger(del1)) {
      num2 = del1;
      break;
    }
  }
  let x = num1 - num2;
  let y = num1 + num2;

  return { x: x, y: y };
}
export default Facto;
