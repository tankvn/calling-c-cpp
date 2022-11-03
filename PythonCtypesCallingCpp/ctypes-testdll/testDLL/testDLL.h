#if !defined(_WIN32) && !defined(_WIN64)
#define EXPORT_API
#else
#define EXPORT_API __declspec(dllexport)
#endif

#ifdef __cplusplus
extern "C" {
#endif

EXPORT_API void testDLL(const int i);

#ifdef __cplusplus
}
#endif