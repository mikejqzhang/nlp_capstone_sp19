# Blog Post 7

## More experiments
|------------------------------------+--------------------+----------------------------|
| Model                              |  IMDB Dev Accuracy | StackOverflow Dev Accuracy |
|                                    | (2 output classes) |        (20 output classes) |
|------------------------------------+--------------------+----------------------------|
| baseline                           |             0.9080 |                     0.8483 |
| dwac                               |             0.9068 |                     0.7661 |
| dwac, batch size = 64              |                  - |                     0.8661 |
|------------------------------------+--------------------+----------------------------|
| proto_dwac, 1 prototypes/class     |             0.8976 |                     0.8606 |
| proto_dwac, 4 prototypes/class     |             0.9220 |                     0.8433 |
| proto_dwac, 16 prototypes/class    |             0.9076 |                     0.8417 |
| proto_dwac, 64 prototypes/class    |             0.9124 |                     0.8356 |
| proto_dwac, 256 prototypes/class   |             0.9120 |                     0.8511 |
| proto_dwac, 1024 prototypes/class  |             0.9164 |                     0.8467 |
|------------------------------------+--------------------+----------------------------|

## Error analysis

## Next action plan

## Summary of the group feedback discussion
