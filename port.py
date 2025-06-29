import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="resource/port.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self, skills=None):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=str(row["Platfrom"]),
                       metadatas={"Links": str(row["Link"])},
                       ids=[str(uuid.uuid4())])
        if skills:
            return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
        return []

    def query_links(self, skills):
        """Query the portfolio collection for relevant links based on skills"""
        if not skills:
            return []
        
        # Convert skills list to a single string for querying
        skills_text = " ".join(skills) if isinstance(skills, list) else str(skills)
        
        results = self.collection.query(
            query_texts=[skills_text], 
            n_results=2
        )
        
        # Extract links from metadata
        links = []
        if results and 'metadatas' in results:
            for metadata_list in results['metadatas']:
                for metadata in metadata_list:
                    if 'Links' in metadata:
                        links.append(metadata['Links'])
        
        return links

