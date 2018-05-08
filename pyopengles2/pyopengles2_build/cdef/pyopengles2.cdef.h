typedef float khronos_float_t;

typedef khronos_float_t GLfloat;
typedef unsigned int GLbitfield;
typedef unsigned int GLuint;
typedef unsigned int GLenum;
typedef int GLsizei;
typedef char GLchar;
typedef int GLint;
typedef unsigned char GLboolean;

void glClear(GLbitfield mask);
void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha);
GLuint glCreateProgram(void);
GLuint glCreateShader(GLenum type);
void glShaderSource(GLuint shader, GLsizei count, const GLchar *const*string, const GLint *length);
void glCompileShader(GLuint shader);
void glGetShaderiv(GLuint shader, GLenum pname, GLint *params);
void glGetShaderInfoLog(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog);
void glDeleteShader(GLuint shader);
void glAttachShader(GLuint program, GLuint shader);
void glLinkProgram(GLuint program);
void glGetProgramiv(GLuint program, GLenum pname, GLint *params);
void glGetProgramInfoLog(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog);
void glDeleteProgram(GLuint program);
GLint glGetAttribLocation(GLuint program, const GLchar *name);
GLint glGetUniformLocation(GLuint program, const GLchar *name);
void glGenBuffers(GLsizei n, GLuint *buffers);
void glBindBuffer(GLenum target, GLuint buffer);
void glBufferData(GLenum target, GLsizeiptr size, const void *data, GLenum usage);
void glVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer);
void glEnableVertexAttribArray (GLuint index);
void glUseProgram(GLuint program);
