# VE-F2-001 — Raw Artifact SHA-256 Manifest

The values below were calculated after execution. `raw/` artifacts are original
execution materials; this manifest is a controlled derivative. The three F2
fixture values are the controlled-input verification values.

| Artifact | SHA-256 |
| --- | --- |
| `F2/bootstrap.toml` | `43200ab70e358eb7b707e5f9f1d6249fc5654c14d7abac810b24ac1c062486a3` |
| `F2/project.toml` | `b4f9da23069f44f5881eae06adf062d3f943b3b3ac81651eb149dca02e20f26f` |
| `F2/sources/atlas-boundaries.md` | `f181116ab9ed88568843c0fe56c674e5bed8cfc113bd0487a3d504f74ce6d71a` |
| `raw/bootstrap-validate-py314.stdout` | `d3175fe8e5d22fd622d003d656efc75a9ced5d4cb155bb927a8af730c91a1851` |
| `raw/bootstrap-validate-py314.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `raw/bootstrap-validate.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `raw/bootstrap-validate.stderr` | `d5fc4556bcd9138a80d56c28419f6c3758f29e88db2ec00a0a06d1b8335d06ea` |
| `raw/f2-execution.py` | `11b921bc7ca95757ce0a7c9790c045e341b068071cce21cf682ad78c61d926c3` |
| `raw/f2-execution-py314.stdout` | `bc0f90aa6c51b1748beea7eeffdeffddabbfe5afb71f786c8e695183b5224834` |
| `raw/f2-execution-py314.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `raw/f2-execution.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `raw/f2-execution.stderr` | `d5fc4556bcd9138a80d56c28419f6c3758f29e88db2ec00a0a06d1b8335d06ea` |
| `raw/f2-state.sqlite` | `8367fb0606c156afe6511ac473b09b74192c68086004822c091a94bb8821b386` |
| `raw/raw-result.json` | `1ad9e06afca506ca7d48cb26aaf646fe4ef9c282fdeee146a4581710fe7117d7` |
| `raw/rendering-human.md` | `b0a7f0765e825f107a2680f82d5b59322f7c69e3004a730248a20352d7091983` |
| `raw/rendering-chatgpt.md` | `29d90d897b3048a346d30d5d1bd153d6fbd6d5b0fd7903daf8fbf6a3cf2ea5b6` |
| `raw/rendering-codex.md` | `dea61f5da98c1111e544759d80540fa2bc711eb51bc6606c1d5eeaf9e015174f` |

The unqualified `bootstrap-validate.*` and `f2-execution.*` artifacts retain
the failed non-semantic interpreter invocation (`python` was unavailable);
the `*-py314.*` artifacts are the successful controlled F2 execution using
Python 3.14.4. The former did not enter bootstrap or pipeline behavior and is
not a second fixture result.
