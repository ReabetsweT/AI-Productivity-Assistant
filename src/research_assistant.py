"""
Research Assistant Module
Handles research tasks, document analysis, and information synthesis
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

class ResearchAssistant:
    """Assists with research tasks and information synthesis"""
    
    def __init__(self):
        self.api_key = os.getenv('google_api_key')
        if not self.api_key:
            raise ValueError("Google API key not found in environment variables")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def analyze_documents(self, documents, query):
        """
        Analyze multiple documents and extract relevant information
        
        Args:
            documents (list): List of document texts
            query (str): Research query
        
        Returns:
            dict: Analysis results with key findings
        """
        docs_combined = "\n\n---\n\n".join(documents)
        
        prompt = f"""Analyze the following documents to answer this research query:

Query: {query}

Documents:
{docs_combined}

Provide a JSON response with: key_findings (list), supporting_evidence (list), gaps_in_research (list), and recommendations (list)."""
        
        try:
            response = self.model.generate_content(prompt)
            
            try:
                # Try to parse as JSON
                result = json.loads(response.text)
                return result
            except json.JSONDecodeError:
                # Return response as structured data
                return {
                    "key_findings": [response.text[:500]],
                    "supporting_evidence": [],
                    "gaps_in_research": [],
                    "recommendations": [],
                    "full_response": response.text
                }
        except Exception as e:
            print(f"Error analyzing documents: {e}")
            return {
                "key_findings": [],
                "supporting_evidence": [],
                "gaps_in_research": [],
                "recommendations": [f"Error: {str(e)}"]
            }
    
    def generate_citations(self, sources, style="APA"):
        """
        Generate citations from source materials
        
        Args:
            sources (list): List of source information
            style (str): Citation style (APA, MLA, Chicago)
        
        Returns:
            dict: Formatted citations
        """
        sources_str = "\n".join([f"- {source}" for source in sources])
        
        prompt = f"""Generate {style} style citations for these sources:

{sources_str}

Return a JSON with 'citations' (list) and 'bibliography' (formatted text)."""
        
        try:
            response = self.model.generate_content(prompt)
            
            try:
                return json.loads(response.text)
            except json.JSONDecodeError:
                return {
                    "citations": response.text.split('\n'),
                    "bibliography": response.text,
                    "style": style
                }
        except Exception as e:
            print(f"Error generating citations: {e}")
            return {"error": str(e)}
    
    def synthesize_information(self, topic, sources):
        """
        Synthesize information from multiple sources
        
        Args:
            topic (str): Research topic
            sources (list): List of source materials
        
        Returns:
            str: Synthesized research report
        """
        sources_str = "\n\n".join([f"Source {i+1}:\n{source}" for i, source in enumerate(sources)])
        
        prompt = f"""Synthesize information about '{topic}' from these sources:

{sources_str}

Create a comprehensive research report with:
1. Overview
2. Key themes
3. Conclusions
4. Recommendations for further research"""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error synthesizing information: {e}")
            return f"Error generating report: {str(e)}"
    
    def research_query(self, query):
        """
        Perform research on a general query
        
        Args:
            query (str): Research question
        
        Returns:
            str: Research findings
        """
        prompt = f"""Provide comprehensive research findings for: {query}

Include:
1. Overview
2. Key points
3. Supporting evidence
4. Counterarguments
5. Conclusion"""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error researching query: {e}")
            return f"Error: {str(e)}"
