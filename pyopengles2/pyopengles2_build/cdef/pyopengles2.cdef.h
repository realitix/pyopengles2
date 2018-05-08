typedef float khronos_float_t;

typedef khronos_float_t GLfloat;
typedef unsigned int GLbitfield;
typedef unsigned int GLuint;
typedef unsigned int GLenum;
typedef int GLsizei;
typedef char GLchar;
typedef int GLint;

void glClear(GLbitfield mask);
void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
GLuint glCreateProgram(void);
GLuint glCreateShader(GLenum type);
void glShaderSource(GLuint shader, GLsizei count, const GLchar *const*string, const GLint *length);
void glCompileShader(GLuint shader);
