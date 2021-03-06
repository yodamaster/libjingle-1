# Copyright (c) 2013 The WebRTC project authors.All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'targets': [
    {
      'target_name': 'video_tests_common',
      'type': 'static_library',
      'sources': [
        'common/file_capturer.cc',
        'common/file_capturer.h',
        'common/flags.cc',
        'common/flags.h',
        'common/frame_generator.cc',
        'common/frame_generator.h',
        'common/frame_generator_capturer.cc',
        'common/frame_generator_capturer.h',
        'common/generate_ssrcs.h',
        'common/gl/gl_renderer.cc',
        'common/gl/gl_renderer.h',
        'common/linux/glx_renderer.cc',
        'common/linux/glx_renderer.h',
        'common/linux/video_renderer_linux.cc',
        'common/mac/run_tests.mm',
        'common/mac/video_renderer_mac.h',
        'common/mac/video_renderer_mac.mm',
        'common/null_platform_renderer.cc',
        'common/run_tests.cc',
        'common/run_tests.h',
        'common/run_loop.cc',
        'common/run_loop.h',
        'common/statistics.cc',
        'common/statistics.h',
        'common/vcm_capturer.cc',
        'common/vcm_capturer.h',
        'common/video_capturer.cc',
        'common/video_capturer.h',
        'common/video_renderer.cc',
        'common/video_renderer.h',
        'common/win/d3d_renderer.cc',
        'common/win/d3d_renderer.h',
        'common/win/run_loop_win.cc',
      ],
      'conditions': [
        ['OS=="linux"', {
          'sources!': [
            'common/null_platform_renderer.cc',
          ],
        }],
        ['OS=="mac"', {
          'sources!': [
            'common/null_platform_renderer.cc',
            'common/run_tests.cc',
          ],
        }],
        ['OS!="linux" and OS!="mac"', {
          'sources!' : [
            'common/gl/gl_renderer.cc',
            'common/gl/gl_renderer.h',
          ],
        }],
        ['OS=="win"', {
          'sources!': [
            'common/null_platform_renderer.cc',
            'common/run_loop.cc',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'conditions': [
          ['OS=="linux"', {
            'libraries': [
              '-lXext',
              '-lX11',
              '-lGL',
            ],
          }],
          #TODO(pbos) : These dependencies should not have to be here, they
          #             aren't used by test code directly, only by components
          #             used by the tests.
          ['OS=="android"', {
            'libraries' : [
              '-lGLESv2', '-llog',
            ],
          }],
          ['OS=="mac"', {
            'xcode_settings' : {
              'OTHER_LDFLAGS' : [
                '-framework Foundation',
                '-framework AppKit',
                '-framework Cocoa',
                '-framework OpenGL',
                '-framework CoreVideo',
                '-framework CoreAudio',
                '-framework AudioToolbox',
              ],
            },
          }],
        ],
      },
      'dependencies': [
        '<(DEPTH)/testing/gtest.gyp:gtest',
        '<(DEPTH)/third_party/google-gflags/google-gflags.gyp:google-gflags',
        '<(webrtc_root)/modules/modules.gyp:video_capture_module',
        'video_engine_core',
      ],
    },
    {
      'target_name': 'video_loopback',
      'type': 'executable',
      'sources': [
        'loopback.cc',
        'test_main.cc',
      ],
      'dependencies': [
        '<(DEPTH)/testing/gtest.gyp:gtest',
        'video_tests_common',
      ],
    },
    {
      'target_name': 'video_full_stack',
      'type': 'executable',
      'sources': [
        'full_stack.cc',
        'test_main.cc',
      ],
      'dependencies': [
        '<(DEPTH)/testing/gtest.gyp:gtest',
        '<(DEPTH)/third_party/google-gflags/google-gflags.gyp:google-gflags',
        '<(webrtc_root)/test/test.gyp:test_support',
        'video_tests_common',
      ],
    },
  ],
}
