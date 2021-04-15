"""
All or portions of this file Copyright (c) Amazon.com, Inc. or its affiliates or
its licensors.

For complete copyright and license terms please see the LICENSE at the root of this
distribution (the "License"). All use of this software is governed by the License,
or, if provided, by the license below or the license accompanying this file. Do not
remove or modify any license notices. This file is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""

"""
C24064534: The View menu options function normally
"""

import os
import sys

import azlmbr.paths

sys.path.append(os.path.join(azlmbr.paths.devroot, 'AutomatedTesting', 'Gem', 'PythonTests'))
from automatedtesting_shared.editor_test_helper import EditorTestHelper
import automatedtesting_shared.pyside_utils as pyside_utils


class TestViewMenuOptions(EditorTestHelper):
    def __init__(self):
        EditorTestHelper.__init__(self, log_prefix="Menus_EditMenuOptions", args=["level"])

    def run_test(self):
        """
        Summary:
        Interact with View Menu options and verify if all the options are working.

        Expected Behavior:
        The View menu functions normally.

        Test Steps:
         1) Create a temp level
         2) Interact with View Menu options

        Note:
        - This test file must be called from the Lumberyard Editor command terminal
        - Any passed and failed tests are written to the Editor.log file.
                Parsing the file or running a log_monitor are required to observe the test results.

        :return: None
        """
        view_menu_options = [
            ("Center on Selection",),
            ("Show Quick Access Bar",),
            ("Viewport", "Wireframe"),
            ("Viewport", "Grid Settings"),
            ("Viewport", "Go to Position"),
            ("Viewport", "Center on Selection"),
            ("Viewport", "Go to Location"),
            ("Viewport", "Remember Location"),
            ("Viewport", "Change Move Speed"),
            ("Viewport", "Switch Camera"),
            ("Viewport", "Show/Hide Helpers"),
            ("Refresh Style",),
        ]

        # 1) Create and open the temp level
        self.test_success = self.create_level(
            self.args["level"],
            heightmap_resolution=1024,
            heightmap_meters_per_pixel=1,
            terrain_texture_resolution=4096,
            use_terrain=False,
        )

        def on_action_triggered(action_name):
            print(f"{action_name} Action triggered")

        # 2) Interact with View Menu options
        try:
            editor_window = pyside_utils.get_editor_main_window()
            for option in view_menu_options:
                action = pyside_utils.get_action_for_menu_path(editor_window, "View", *option)
                trig_func = lambda: on_action_triggered(action.iconText())
                action.triggered.connect(trig_func)
                action.trigger()
                action.triggered.disconnect(trig_func)
        except Exception as e:
            self.test_success = False
            print(e)


test = TestViewMenuOptions()
test.run()