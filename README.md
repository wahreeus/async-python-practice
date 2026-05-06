# Async Python Practice

This repository contains two complementary sets of Python concurrency exercises:

1. **Async Python Practice** — 50 `asyncio` implementation and debugging exercises focused on practical async patterns.
2. **Sync To Async Python Practice** — 20 transformation exercises where an existing blocking Python program must be rewritten as an async version.

Together, the sets cover core `asyncio` mechanics, task orchestration, queues, timeouts, cancellation, rate limiting, worker pools, async pipelines, and the practical skill of converting synchronous I/O-heavy code into asynchronous code.

## Structure

- **70 exercises total**
  - **50 core async exercises**
  - **20 sync-to-async transformation exercises**
- Core async set:
  - **40 implementation tasks**
  - **10 debugging tasks**
  - Difficulty progression: **Easy → Easy-medium → Medium → Medium-hard → Hard**
- Sync-to-async set:
  - **20 transformation tasks** based on blocking programs
  - Difficulty progression: **Easy → Easy-medium → Medium → Medium-hard → Hard**
  - Focuses on converting real-world synchronous I/O patterns into async designs
- Debugging tasks use valid Python syntax and focus on logical or runtime issues rather than formatting or syntax errors

## Exercise sets

| Set | File | Exercises | Focus |
|---|---|:---:|---|
| Async Python Practice | `async-python-practice.pdf` | 50 | Standalone async implementation and debugging tasks. |
| Sync To Async Python Practice | `sync_to_async-python-practice.pdf` | 20 | Transform blocking HTTP, parsing, caching, and pipeline programs into async versions. |

## Async Python Practice exercise index

| # | Exercise | Level | Type | Main focus |
|---:|---|:---:|:---:|---|
| 1 | Awaited mock requests | Easy | Implementation | Await simple simulated I/O requests in input order. |
| 2 | Completion order with create_task | Easy | Implementation | Create tasks and report results by completion order. |
| 3 | Gathered API statuses | Easy | Implementation | Use gather while preserving input-order results. |
| 4 | Async uppercase transform | Easy | Implementation | Run delayed transformations concurrently. |
| 5 | Missing await in delayed doubles | Easy | **Debugging** | Fix unawaited coroutines and collect numeric results. |
| 6 | as_completed result stream | Easy | Implementation | Stream task results as jobs finish. |
| 7 | Scheduled timer events | Easy | Implementation | Schedule timer events with tie handling. |
| 8 | Per-task timeout | Easy | Implementation | Apply timeout logic to concurrent requests. |
| 9 | Shard count collector | Easy | Implementation | Collect concurrent shard results and summarize them. |
| 10 | Gather used when completion order is required | Easy | **Debugging** | Replace input-order gather behavior with completion-order reporting. |
| 11 | Result and error collection | Easy-medium | Implementation | Collect successes and failures without stopping all tasks. |
| 12 | Bounded concurrent downloader | Easy-medium | Implementation | Limit the number of active jobs. |
| 13 | Single consumer queue | Easy-medium | Implementation | Use producers and one queue consumer. |
| 14 | First successful response | Easy-medium | Implementation | Return the first successful concurrent result. |
| 15 | Queue order bug | Easy-medium | **Debugging** | Fix incorrect queue behavior. |
| 16 | Cancel unfinished jobs | Easy-medium | Implementation | Cancel work that misses a shared cutoff. |
| 17 | Retry flaky endpoints | Easy-medium | Implementation | Implement bounded retry logic. |
| 18 | Periodic ticker | Easy-medium | Implementation | Emit repeated ticks at simulated intervals. |
| 19 | First K completions | Easy-medium | Implementation | Take enough completed results and cancel the rest. |
| 20 | Unawaited gather | Easy-medium | **Debugging** | Fix a gather object used before awaiting. |
| 21 | Batch rate limiter | Medium | Implementation | Assign request starts to per-second buckets. |
| 22 | Priority queue workers | Medium | Implementation | Feed worker tasks from a priority queue. |
| 23 | Sequential batches, concurrent inside each batch | Medium | Implementation | Run each batch concurrently, but batches sequentially. |
| 24 | Per-key async cache | Medium | Implementation | Share one fetch among concurrent requests for the same key. |
| 25 | Async counter race | Medium | **Debugging** | Fix a race condition around shared state. |
| 26 | Deadline-aware steps | Medium | Implementation | Run multi-step jobs while respecting deadlines. |
| 27 | Fan-out fan-in pipeline | Medium | Implementation | Coordinate download and transform stages. |
| 28 | Graceful queue shutdown | Medium | Implementation | Stop workers cleanly with sentinel values. |
| 29 | Per-host concurrency cap | Medium | Implementation | Limit concurrency independently per host. |
| 30 | Swallowed cancellation | Medium | **Debugging** | Fix cancellation that is incorrectly converted into success. |
| 31 | Token bucket scheduler | Medium-hard | Implementation | Simulate token-bucket request scheduling. |
| 32 | Async dependency DAG | Medium-hard | Implementation | Run tasks once dependencies complete. |
| 33 | Fail-fast gather | Medium-hard | Implementation | Stop all work when the first failure appears. |
| 34 | Backpressure with bounded queue | Medium-hard | Implementation | Model producers waiting on a full queue. |
| 35 | wait_for cancels a shared task | Medium-hard | **Debugging** | Protect a shared task from timeout cancellation. |
| 36 | Bounded async map unordered | Medium-hard | Implementation | Map values with limited concurrency and unordered output. |
| 37 | Inactivity batch timer | Medium-hard | Implementation | Group events using an inactivity timeout. |
| 38 | Two-stage worker pipeline | Medium-hard | Implementation | Coordinate separate worker pools across stages. |
| 39 | Supervisor cancellation tree | Medium-hard | Implementation | Cancel child tasks when one fails. |
| 40 | Lock release on failure | Medium-hard | **Debugging** | Ensure locks are released after exceptions. |
| 41 | Per-domain dynamic rate limits | Hard | Implementation | Apply independent per-domain request limits. |
| 42 | Earliest-deadline async scheduler | Hard | Implementation | Choose available jobs by earliest deadline. |
| 43 | Async circuit breaker simulation | Hard | Implementation | Implement open, half-open, and closed breaker states. |
| 44 | Adaptive concurrency batches | Hard | Implementation | Adjust batch concurrency based on latency. |
| 45 | Semaphore leak on exception | Hard | **Debugging** | Prevent semaphore permits from leaking on failure. |
| 46 | Concurrent log stream merger | Hard | Implementation | Merge asynchronous streams by arrival time. |
| 47 | Cancellation-safe pipeline summary | Hard | Implementation | Summarize pipeline state after cancellation. |
| 48 | Total timeout budget with retries | Hard | Implementation | Share one timeout budget across retry attempts. |
| 49 | Bounded async crawler | Hard | Implementation | Crawl a graph with depth and per-host limits. |
| 50 | Duplicate async cache fetches | Hard | **Debugging** | Ensure concurrent cache misses share one in-flight fetch. |

## Sync To Async Python Practice exercise index

| # | Exercise | Level | Type | Main focus |
|---:|---|:---:|:---:|---|
| 1 | Page status and size report | Easy | Transformation | Fetch multiple pages concurrently while preserving input-order output. |
| 2 | Completion-order page fetches | Easy | Transformation | Start all fetches first and print each result as soon as it completes. |
| 3 | Bounded JSON record lookup | Easy-medium | Transformation | Convert a sequential JSON client into a bounded-concurrency async client. |
| 4 | Repository metadata report | Easy-medium | Transformation | Fetch repository metadata concurrently while keeping formatting logic explicit. |
| 5 | Bounded HEAD request checker | Easy-medium | Transformation | Convert blocking HEAD checks into bounded async checks. |
| 6 | Package metadata collector | Medium | Transformation | Fetch package metadata concurrently while preserving input-order reporting. |
| 7 | HTML title scraper | Medium | Transformation | Convert a blocking title scraper into concurrent async page fetches. |
| 8 | Per-request timeout report | Medium | Transformation | Apply per-request timeouts without stopping unrelated requests. |
| 9 | JSON field extractor | Medium | Transformation | Fetch JSON documents concurrently while keeping field extraction separate. |
| 10 | Download checksum report | Medium | Transformation | Download files concurrently while keeping deterministic hashing and ordered output. |
| 11 | CSV row counter | Medium | Transformation | Overlap CSV downloads while parsing each document into a row count. |
| 12 | Sequential retry chains | Medium-hard | Transformation | Run different retry chains concurrently while keeping attempts sequential per row. |
| 13 | Legacy downloader bridge | Medium-hard | Transformation | Use a blocking helper safely from async code without changing the helper itself. |
| 14 | Paginated API chains | Medium-hard | Transformation | Run collections concurrently while fetching pages sequentially inside each collection. |
| 15 | Per-origin request queues | Medium-hard | Transformation | Allow different origins to run concurrently while keeping same-origin requests sequential. |
| 16 | Shared webpage cache | Hard | Transformation | Share one in-flight fetch for duplicate URLs while allowing distinct URLs to proceed. |
| 17 | Mirror race for assets | Hard | Transformation | Race mirrors for each asset and keep the first successful response. |
| 18 | Freshness verifier with retries | Hard | Transformation | Check resources concurrently while keeping retry decisions local to each resource. |
| 19 | Blocking parser bridge | Hard | Transformation | Call a blocking parser from async code without freezing other downloads. |
| 20 | Three-stage report pipeline | Hard | Transformation | Build a concurrent download-parse-store pipeline with bounded parse and store stages. |

## Topics covered

`async` / `await`, `asyncio.create_task`, `asyncio.gather`, `asyncio.as_completed`, `asyncio.wait_for`, `asyncio.shield`, timeouts, cancellation, queues, priority queues, semaphores, locks, rate limiting, retries, producer-consumer patterns, worker pools, task dependencies, backpressure, async pipelines, shared in-flight work, cache coordination, and bridging blocking code into async programs.

## Note

Many exercises have a straightforward synchronous solution, but they are intended to be interpreted through an async lens for practice purposes. The sync-to-async exercises are especially meant to practice recognizing where blocking I/O, sequential loops, shared caches, and staged pipelines can be redesigned with async concurrency.