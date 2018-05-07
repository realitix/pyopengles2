from pyegl._pyegl import ffi, lib


EGL_ALPHA_SIZE = 0x3021
EGL_BAD_ACCESS = 0x3002
EGL_BAD_ALLOC = 0x3003
EGL_BAD_ATTRIBUTE = 0x3004
EGL_BAD_CONFIG = 0x3005
EGL_BAD_CONTEXT = 0x3006
EGL_BAD_CURRENT_SURFACE = 0x3007
EGL_BAD_DISPLAY = 0x3008
EGL_BAD_MATCH = 0x3009
EGL_BAD_NATIVE_PIXMAP = 0x300A
EGL_BAD_NATIVE_WINDOW = 0x300B
EGL_BAD_PARAMETER = 0x300C
EGL_BAD_SURFACE = 0x300D
EGL_BLUE_SIZE = 0x3022
EGL_BUFFER_SIZE = 0x3020
EGL_CONFIG_CAVEAT = 0x3027
EGL_CONFIG_ID = 0x3028
EGL_CORE_NATIVE_ENGINE = 0x305B
EGL_DEPTH_SIZE = 0x3025
EGL_DONT_CARE = ffi.cast('EGLint', -1)
EGL_DRAW = 0x3059
EGL_EXTENSIONS = 0x3055
EGL_FALSE = 0
EGL_GREEN_SIZE = 0x3023
EGL_HEIGHT = 0x3056
EGL_LARGEST_PBUFFER = 0x3058
EGL_LEVEL = 0x3029
EGL_MAX_PBUFFER_HEIGHT = 0x302A
EGL_MAX_PBUFFER_PIXELS = 0x302B
EGL_MAX_PBUFFER_WIDTH = 0x302C
EGL_NATIVE_RENDERABLE = 0x302D
EGL_NATIVE_VISUAL_ID = 0x302E
EGL_NATIVE_VISUAL_TYPE = 0x302F
EGL_NONE = 0x3038
EGL_NON_CONFORMANT_CONFIG = 0x3051
EGL_NOT_INITIALIZED = 0x3001
EGL_NO_CONTEXT = ffi.cast('EGLContext', 0)
EGL_NO_DISPLAY = ffi.cast('EGLDisplay', 0)
EGL_NO_SURFACE = ffi.cast('EGLSurface', 0)
EGL_PBUFFER_BIT = 0x0001
EGL_PIXMAP_BIT = 0x0002
EGL_READ = 0x305A
EGL_RED_SIZE = 0x3024
EGL_SAMPLES = 0x3031
EGL_SAMPLE_BUFFERS = 0x3032
EGL_SLOW_CONFIG = 0x3050
EGL_STENCIL_SIZE = 0x3026
EGL_SUCCESS = 0x3000
EGL_SURFACE_TYPE = 0x3033
EGL_TRANSPARENT_BLUE_VALUE = 0x3035
EGL_TRANSPARENT_GREEN_VALUE = 0x3036
EGL_TRANSPARENT_RED_VALUE = 0x3037
EGL_TRANSPARENT_RGB = 0x3052
EGL_TRANSPARENT_TYPE = 0x3034
EGL_TRUE = 1
EGL_VENDOR = 0x3053
EGL_VERSION = 0x3054
EGL_WIDTH = 0x3057
EGL_WINDOW_BIT = 0x0004
EGL_BACK_BUFFER = 0x3084
EGL_BIND_TO_TEXTURE_RGB = 0x3039
EGL_BIND_TO_TEXTURE_RGBA = 0x303A
EGL_CONTEXT_LOST = 0x300E
EGL_MIN_SWAP_INTERVAL = 0x303B
EGL_MAX_SWAP_INTERVAL = 0x303C
EGL_MIPMAP_TEXTURE = 0x3082
EGL_MIPMAP_LEVEL = 0x3083
EGL_NO_TEXTURE = 0x305C
EGL_TEXTURE_2D = 0x305F
EGL_TEXTURE_FORMAT = 0x3080
EGL_TEXTURE_RGB = 0x305D
EGL_TEXTURE_RGBA = 0x305E
EGL_TEXTURE_TARGET = 0x3081
EGL_ALPHA_FORMAT = 0x3088
EGL_ALPHA_FORMAT_NONPRE = 0x308B
EGL_ALPHA_FORMAT_PRE = 0x308C
EGL_ALPHA_MASK_SIZE = 0x303E
EGL_BUFFER_PRESERVED = 0x3094
EGL_BUFFER_DESTROYED = 0x3095
EGL_CLIENT_APIS = 0x308D
EGL_COLORSPACE = 0x3087
EGL_COLORSPACE_sRGB = 0x3089
EGL_COLORSPACE_LINEAR = 0x308A
EGL_COLOR_BUFFER_TYPE = 0x303F
EGL_CONTEXT_CLIENT_TYPE = 0x3097
EGL_DISPLAY_SCALING = 10000
EGL_HORIZONTAL_RESOLUTION = 0x3090
EGL_LUMINANCE_BUFFER = 0x308F
EGL_LUMINANCE_SIZE = 0x303D
EGL_OPENGL_ES_BIT = 0x0001
EGL_OPENVG_BIT = 0x0002
EGL_OPENGL_ES_API = 0x30A0
EGL_OPENVG_API = 0x30A1
EGL_OPENVG_IMAGE = 0x3096
EGL_PIXEL_ASPECT_RATIO = 0x3092
EGL_RENDERABLE_TYPE = 0x3040
EGL_RENDER_BUFFER = 0x3086
EGL_RGB_BUFFER = 0x308E
EGL_SINGLE_BUFFER = 0x3085
EGL_SWAP_BEHAVIOR = 0x3093
EGL_UNKNOWN = ffi.cast('EGLint', -1)
EGL_VERTICAL_RESOLUTION = 0x3091
EGL_CONFORMANT = 0x3042
EGL_CONTEXT_CLIENT_VERSION = 0x3098
EGL_MATCH_NATIVE_PIXMAP = 0x3041
EGL_OPENGL_ES2_BIT = 0x0004
EGL_VG_ALPHA_FORMAT = 0x3088
EGL_VG_ALPHA_FORMAT_NONPRE = 0x308B
EGL_VG_ALPHA_FORMAT_PRE = 0x308C
EGL_VG_ALPHA_FORMAT_PRE_BIT = 0x0040
EGL_VG_COLORSPACE = 0x3087
EGL_VG_COLORSPACE_sRGB = 0x3089
EGL_VG_COLORSPACE_LINEAR = 0x308A
EGL_VG_COLORSPACE_LINEAR_BIT = 0x0020
EGL_DEFAULT_DISPLAY = ffi.cast('EGLNativeDisplayType', 0)
EGL_MULTISAMPLE_RESOLVE_BOX_BIT = 0x0200
EGL_MULTISAMPLE_RESOLVE = 0x3099
EGL_MULTISAMPLE_RESOLVE_DEFAULT = 0x309A
EGL_MULTISAMPLE_RESOLVE_BOX = 0x309B
EGL_OPENGL_API = 0x30A2
EGL_OPENGL_BIT = 0x0008
EGL_SWAP_BEHAVIOR_PRESERVED_BIT = 0x0400
EGL_CONTEXT_MAJOR_VERSION = 0x3098
EGL_CONTEXT_MINOR_VERSION = 0x30FB
EGL_CONTEXT_OPENGL_PROFILE_MASK = 0x30FD
EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY = 0x31BD
EGL_NO_RESET_NOTIFICATION = 0x31BE
EGL_LOSE_CONTEXT_ON_RESET = 0x31BF
EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT = 0x00000001
EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT = 0x00000002
EGL_CONTEXT_OPENGL_DEBUG = 0x31B0
EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE = 0x31B1
EGL_CONTEXT_OPENGL_ROBUST_ACCESS = 0x31B2
EGL_OPENGL_ES3_BIT = 0x00000040
EGL_CL_EVENT_HANDLE = 0x309C
EGL_SYNC_CL_EVENT = 0x30FE
EGL_SYNC_CL_EVENT_COMPLETE = 0x30FF
EGL_SYNC_PRIOR_COMMANDS_COMPLETE = 0x30F0
EGL_SYNC_TYPE = 0x30F7
EGL_SYNC_STATUS = 0x30F1
EGL_SYNC_CONDITION = 0x30F8
EGL_SIGNALED = 0x30F2
EGL_UNSIGNALED = 0x30F3
EGL_SYNC_FLUSH_COMMANDS_BIT = 0x0001
# EGL_FOREVER = 0xFFFFFFFFFFFFFFFFull
EGL_TIMEOUT_EXPIRED = 0x30F5
EGL_CONDITION_SATISFIED = 0x30F6
EGL_NO_SYNC = ffi.cast('EGLSync', 0)
EGL_SYNC_FENCE = 0x30F9
EGL_GL_COLORSPACE = 0x309D
EGL_GL_COLORSPACE_SRGB = 0x3089
EGL_GL_COLORSPACE_LINEAR = 0x308A
EGL_GL_RENDERBUFFER = 0x30B9
EGL_GL_TEXTURE_2D = 0x30B1
EGL_GL_TEXTURE_LEVEL = 0x30BC
EGL_GL_TEXTURE_3D = 0x30B2
EGL_GL_TEXTURE_ZOFFSET = 0x30BD
EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x30B3
EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x30B4
EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x30B5
EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x30B6
EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x30B7
EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x30B8
EGL_IMAGE_PRESERVED = 0x30D2
EGL_NO_IMAGE = ffi.cast('EGLImage', 0)


class EglError(Exception):
    pass


_errors = {
    EGL_NOT_INITIALIZED: "EGL is not initialized, or could not be initialized, for the specified EGL display connection.",  # noqa
    EGL_BAD_ACCESS: "EGL cannot access a requested resource (for example a context is bound in another thread).",  # noqa
    EGL_BAD_ALLOC: "EGL failed to allocate resources for the requested operation.",  # noqa
    EGL_BAD_ATTRIBUTE: "An unrecognized attribute or attribute value was passed in the attribute list. ",  # noqa
    EGL_BAD_CONFIG: "An EGLConfig argument does not name a valid EGL frame buffer configuration.",  # noqa
    EGL_BAD_CONTEXT: "An EGLContext argument does not name a valid EGL rendering context.",  # noqa
    EGL_BAD_CURRENT_SURFACE: "The current surface of the calling thread is a window, pixel buffer or pixmap that is no longer valid.",  # noqa
    EGL_BAD_DISPLAY: "An EGLDisplay argument does not name a valid EGL display connection.",  # noqa
    EGL_BAD_MATCH: "Arguments are inconsistent (for example, a valid context requires buffers not supplied by a valid surface).",  # noqa
    EGL_BAD_NATIVE_PIXMAP: "A NativePixmapType argument does not refer to a valid native pixmap.",  # noqa
    EGL_BAD_NATIVE_WINDOW: "A NativeWindowType argument does not refer to a valid native window.",  # noqa
    EGL_BAD_PARAMETER: "One or more argument values are invalid.",  # noqa
    EGL_BAD_SURFACE: "An EGLSurface argument does not name a valid surface (window, pixel buffer or pixmap) configured for GL rendering.",  # noqa
    EGL_CONTEXT_LOST: "A power management event has occurred. The application must destroy all contexts and reinitialise OpenGL ES state and objects to continue rendering."  # noqa
}


def _check(result):
    code = lib.eglGetError()
    if code == EGL_SUCCESS:
        return result

    raise EglError(_errors[code])


def eglGetDisplay(display_id):
    return lib.eglGetDisplay(display_id)


def eglInitialize(display):
    major = ffi.new('EGLint*')
    minor = ffi.new('EGLint*')
    _check(lib.eglInitialize(display, major, minor))

    return major[0], minor[0]


def eglGetConfigs(display):
    num_config = ffi.new('EGLint*')
    _check(lib.eglGetConfigs(display, ffi.NULL, 0, num_config))

    configs = ffi.new('EGLConfig[]', num_config[0])
    _check(lib.eglGetConfigs(display, configs, num_config[0], num_config))

    return configs


def eglChooseConfig(display, attrib_list):
    num_config = ffi.new('EGLint*')
    _check(lib.eglChooseConfig(display, attrib_list, ffi.NULL, 0, num_config))

    configs = ffi.new('EGLConfig[]', num_config[0])
    _check(lib.eglChooseConfig(display, attrib_list, configs, num_config[0],
                               num_config))

    return configs


def eglCreateWindowSurface(display, config, window, attrib_list):
    if not attrib_list:
        attrib_list = ffi.NULL

    return _check(lib.eglCreateWindowSurface(
        display, config, window, attrib_list))


def eglCreateContext(display, config, share_context, attrib_list):
    return _check(lib.eglCreateContext(
        display, config, share_context, attrib_list))


def eglMakeCurrent(display, draw, read, context):
    _check(lib.eglMakeCurrent(
        display, draw, read, context))


def eglSwapBuffers(display, surface):
    _check(lib.eglSwapBuffers(display, surface))


def eglGetConfigAttrib(display, config, attribute):
    value = ffi.new('EGLint*')
    _check(lib.eglGetConfigAttrib(display, config, attribute, value))
    return value[0]
