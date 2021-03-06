# Copyright 2012-2018 CERN for the benefit of the ATLAS collaboration.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors:
# - Vincent Garonne <vgaronne@gmail.com>, 2012-2018
# - Frank Berghaus <frank.berghaus@cern.ch>, 2018


# List of authorized value types for key
try:
    AUTHORIZED_VALUE_TYPES = (float, int, unicode)
except NameError:
    AUTHORIZED_VALUE_TYPES = (float, int, str)

# unicode no longer exists in python3, hence this workaround
try:
    STRING_TYPES = (str, unicode,)
except NameError:
    STRING_TYPES = (str,)
