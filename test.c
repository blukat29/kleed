int check(int a)
{
    if (a == 7) return 1;
    else return 0;
}

int main()
{
    int a;
    klee_make_symbolic(&a, sizeof(a), "aa");
    return check(a);
}
