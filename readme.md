# Sriracha
> I put that on everything!

Sriracha is a MVC web framework written in Python with the purpose of making
big web applications easy, it serves as the Python equivalent of something like
Rails for Ruby, Spring for Java, and could be seen somewhat similar to Angular.

# Quick Start
```bash
python3 -m pip install sri
sri new myproject
cd myproject
./bin/dev-start
```

# FAQ
## Can I use it?
~~Sure, go ahead. You can get started with [Quick Start](#quick-start)~~
Nope, haven't uploaded it to Pyπ yet.

## What templating engine does it use?
[Liquid](https://shopify.github.io/liquid/),
[this](https://github.com/jg-rp/liquid) implementation. If you have experience
with Jekyll or Shopify, you might be familiar with its syntax.

## Is it fast?
That depends on your WSGI server! (sometimes.)

I chose [Gunicorn](https://gunicorn.org/) and did a benchmark using [wrk](https://github.com/wg/wrk):
```
$ gunicorn http://0.0.0.0:8000
Running 10s test @ http://0.0.0.0:8000
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.21ms  336.15us  12.99ms   92.05%
    Req/Sec     1.55k    62.25     1.65k    75.50%
  30797 requests in 10.00s, 11.06MB read
Requests/sec:   3079.11
Transfer/sec:      1.11MB
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
    Latency     1.34ms  126.20us   5.88ms   97.70%
    Req/Sec     3.66k   234.92     6.84k    97.51%
  73109 requests in 10.10s, 10.67MB read
Requests/sec:   7238.95
Transfer/sec:      1.06MB
```
