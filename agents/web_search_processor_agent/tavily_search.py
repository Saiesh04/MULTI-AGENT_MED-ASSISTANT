import requests
from langchain_community.tools.tavily_search import TavilySearchResults

class TavilySearchAgent:
    """
    Processes general documents for the RAG system with context-aware chunking.
    """
    def __init__(self):
        """
        Initialize the Tavily search agent.
        
        Args:
            query: User query
        """
        pass

    def search_tavily(self, query: str) -> str:
        """Perform a general web search using Tavily API."""
        
        import os
        tavily_api_key = os.getenv("TAVILY_API_KEY")
        
        print(f"[TavilySearch] Searching for: {query}")
        print(f"[TavilySearch] API key configured: {bool(tavily_api_key)}")
        
        if not tavily_api_key or tavily_api_key.strip() == "" or tavily_api_key == "your_tavily_api_key_here":
            return "Web search is disabled. Tavily API key not configured."

        tavily_search = TavilySearchResults(max_results = 5)

        # url = "https://api.tavily.com/search"
        # params = {
        #     "api_key": tavily_api_key,
        #     "query": query,
        #     "num_results": 5
        # }
        
        try:
            # Strip any surrounding quotes from the query
            query = query.strip('"\'')
            print(f"[TavilySearch] Cleaned query: {query}")
            
            search_docs = tavily_search.invoke(query)
            print(f"[TavilySearch] Found {len(search_docs)} results")
            
            if len(search_docs):
                results = "\n".join(["title: " + str(res["title"]) + " - " + 
                                  "url: " + str(res["url"]) + " - " + 
                                  "content: " + str(res["content"]) + " - " + 
                                  "score: " + str(res["score"]) for res in search_docs])
                print(f"[TavilySearch] Results preview: {results[:200]}...")
                return results
            return "No relevant results found."
        except Exception as e:
            print(f"[TavilySearch] Error: {str(e)}")
            return f"Error retrieving web search results: {e}"