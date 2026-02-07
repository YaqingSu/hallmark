# Copyright 2026 the Hallmark Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pathlib       import Path
from contextlib    import chdir
from click.testing import CliRunner

from hallmark import Repo


files = [f"a{a}_i{i}.h5"
         for a in [0, 0.75, 0.975]
         for i in [0, 30, 60, 90]]

def test_python():
    runner = CliRunner()
    with runner.isolated_filesystem():
        repo = Repo.init("repo")
        assert Path("repo/.hm").is_dir()

        with chdir("repo"):
            assert Path(".hm").is_dir()
            for file in files:
                Path(file).write_text("test\n", encoding="utf-8")

            result = repo.add("a{a}_i{i}.h5")
            assert len(result) == 12
            assert sorted(result.path) == sorted(files)

            result = repo.commit("Commit test")
            assert result

        repo = Repo("repo")
        assert len(repo.state.data) == 12
        assert repo.worktree.stem == "repo"
