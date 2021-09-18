# C++ Graph Benchmarking

Currently includes the following graph libraries:

- [Boost Graph Library (BGL)](https://www.boost.org/doc/libs/1_77_0/libs/graph/doc/)
- [LEMON](https://lemon.cs.elte.hu/trac/lemon)

And the following benchmarks:

- Dijkstra (with USA distance data)


## Dijkstra

Original source code from:

https://github.com/stegua/MyBlogEntries/tree/master/Dijkstra

Mean and std from solving each instance 50 times changing the source and sink
each time. 

| Solvers        | Instance  | Mean  | Std  |
|----------------|-----------|-------|------|
| Dijkstra_bgl   | USA-d.W   | 1.822 | 0.15 |
| Dijkstra_lemon |           | 0.839 | 0.05 |
| Dijkstra_bgl   | USA-d.E   | 0.966 | 0.03 |
| Dijkstra_lemon |           | 0.565 | 0.01 |
| Dijkstra_bgl   | USA-d.LKS | 0.623 | 0    |
| Dijkstra_lemon |           | 0.061 | 0    |
| Dijkstra_bgl   | USA-d.CAL | 0.433 | 0.01 |
| Dijkstra_lemon |           | 0.151 | 0.03 |
| Dijkstra_bgl   | USA-d.NE  | 0.4   | 0.04 |
| Dijkstra_lemon |           | 0.221 | 0.08 |
| Dijkstra_bgl   | USA-d.NW  | 0.283 | 0.03 |
| Dijkstra_lemon |           | 0.114 | 0.01 |
| Dijkstra_bgl   | USA-d.FLA | 0.208 | 0    |
| Dijkstra_lemon |           | 0.035 | 0    |
| Dijkstra_bgl   | USA-d.COL | 0.089 | 0    |
| Dijkstra_lemon |           | 0.042 | 0.01 |
| Dijkstra_bgl   | USA-d.BAY | 0.068 | 0    |
| Dijkstra_lemon |           | 0.049 | 0    |
| Dijkstra_bgl   | USA-d.NY  | 0.057 | 0    |
| Dijkstra_lemon |           | 0.004 | 0    |

### Pre-requirements

- docker
- docker-compose
- python3

### Run

```bash
cd docker/
docker-compose up --build
python3 results.py
```
