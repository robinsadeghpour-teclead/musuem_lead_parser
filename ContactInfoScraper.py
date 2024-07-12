from scrapegraphai.graphs import SearchGraph

def scrapeContactInfo(museumName):
    graph_config = {
        "llm": {
            "api_key": "YOUR_API_KEY",
            "model": "gpt-3.5-turbo",
        },
        "verbose": True,
    }

    # Create the SearchGraph instance
    search_graph = SearchGraph(
        prompt="Get me the phone number and email of the museum: Museen Aalen",
        config=graph_config,
    )

    try:
        result = search_graph.run()
        return result
    except Exception as e:
        print(f"Error occurred while fetching contact info for {museumName}: {e}")
        return None
