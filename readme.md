# Sriracha
> I put that on everything!

Sriracha is an MVC web framework written in Python with the purpose of making
big and complex web applications easy to maintain, it serves as the Python
equivalent of something like Rails for Ruby, Spring for Java, and could be seen
somewhat similar to Angular.

# Quick Start
```bash
python3 -m pip install sriracha
sri new myproject
cd myproject
./bin/dev-start
```

# FAQ
## Can I use it?
Sure, go ahead. You can get started with [Quick Start](#quick-start)

## What templating engine does it use?
[Liquid](https://shopify.github.io/liquid/),
[this implementation](https://github.com/jg-rp/liquid). If you have experience
with Jekyll or Shopify, you might be familiar with its syntax.

## Is it fast?
That depends on your WSGI server! (sometimes.)

### Benchmark
I chose [Gunicorn](https://gunicorn.org/) with 4 workers and did a benchmark using [wrk](https://github.com/wg/wrk) on my Intel i3-8100 (4) @ 3.600GHz computer

```
$ wrk http://0.0.0.0:8000
Running 10s test @ http://0.0.0.0:8000
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.02ms    1.32ms  21.23ms   94.11%
    Req/Sec     6.03k     1.08k    8.27k    60.50%
  120016 requests in 10.00s, 41.43MB read
Requests/sec:  11999.54
Transfer/sec:      4.14MB
````

Compared to the results of this (which should be much faster as it doesn't have
to do any complex routing or messing with views or controllers):
```python
def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
```

```
Running 10s test @ http://0.0.0.0:8000
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   737.09us    1.23ms  20.51ms   95.06%
    Req/Sec     8.75k     1.09k   10.83k    68.50%
  174307 requests in 10.01s, 25.43MB read
Requests/sec:  17421.07
Transfer/sec:      2.54MB
```
