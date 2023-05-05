# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
import math


class AccelGraph(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def __call__(self, x: float) -> float:
        pass


class SigmoidAccel(AccelGraph):

    def __init__(self, shift_x=5, slope=0.3, multiply=1.2):
        self.shift_x = shift_x
        self.slope = slope
        self.multiply = multiply

    def __call__(self, x: float) -> float:
        x = abs(x)
        sig = 1 / (1 + math.exp(-self.slope * (x - self.shift_x)))
        return self.multiply * sig
