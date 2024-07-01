const binarySearch = function (arr, k, s, e) {
  let s = 0;
  let e = arr.length - 1;
  let mid;
  while (s <= e) {
    mid = parseInt((s + e) / 2);
    if (arr[mid] === k) {
      return mid;
    } else if (arr[mid] > k) {
      e = mid - 1;
    } else {
      s = mid + 1;
    }
  }
  return -1;
};
