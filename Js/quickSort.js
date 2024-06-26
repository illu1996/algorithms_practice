const quickSort = function (arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[0];
  const left = [];
  const right = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }
  let lSorted = quickSort(left);
  let rSorted = quickSort(right);
  return [...lSorted, pivot, ...rSorted];
};

console.log(quickSort([2, 5, 6, 8, 1]));
