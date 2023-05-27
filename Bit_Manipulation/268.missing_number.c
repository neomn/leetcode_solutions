int missingNumber(int *nums, int numsSize) {
  int sum = (numsSize * (numsSize + 1)) / 2, sum2 = 0;
  for (int i = 0; i < numsSize; i++)
    sum2 += nums[i];
  return sum - sum2;
}
