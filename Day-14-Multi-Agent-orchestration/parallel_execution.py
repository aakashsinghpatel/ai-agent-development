import asyncio
import time

async def research_agent():
    print("Started Research Agent")
    await asyncio.sleep(3)
    print("Completed Research Agent")
    return "Research result"

async def technology_agent():
    print("Technology Agent started")
    await asyncio.sleep(2)
    print("Technology Agent finished")
    return "Technology result"


async def market_agent():
    print("Market Agent started")
    await asyncio.sleep(4)
    print("Market Agent finished")
    return "Market result"



async def run_sequential():
    start_time = time.perf_counter()

    research_result = await research_agent()
    technology_result = await technology_agent()
    market_result = await market_agent()

    elapsed = (time.perf_counter()- start_time)

    print("\n Sequential result::")
    print(research_result)
    print(technology_result)
    print(market_result)
    print(f"\nSequential time: "f"{elapsed:.2f} seconds")


async def run_parallel():
    start_time = time.perf_counter()

    results = await asyncio.gather(research_agent(), technology_agent(), market_agent())
    elapsed = (time.perf_counter() - start_time)
    print("\nParallel Results:")
    for result in results:
        print(result)
    print(f"\nParallel time: "f"{elapsed:.2f} seconds")


async def main():
    print("=" * 50)
    print("SEQUENTIAL EXECUTION")
    print("=" * 50)

    await run_sequential()

    print("\n" + "=" * 50)
    print("PARALLEL EXECUTION")
    print("=" * 50)

    await run_parallel()

if __name__ == "__main__":
    asyncio.run(main())