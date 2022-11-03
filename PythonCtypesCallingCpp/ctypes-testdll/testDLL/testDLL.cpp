#include <stdio.h>
​
extern "C" {
​
__declspec(dllexport)
​
void testDLL(const int i) {
    printf("%d\n", i);
}
​
} // extern "C"