int getSum(int a, int b) {
    while (b != 0) {
        int carry = a & b;
        a = a ^ b;
    }
}
