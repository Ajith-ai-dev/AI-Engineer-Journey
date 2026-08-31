Article Link : https://arxiv.org/abs/2510.08558

Fundamental Problem: 

    Can an AI agent learn from its own mistakes and experiences, even when nobody gives it a reward telling it whether it was right or wrong?

### 1. The actual problem:  
    Today's LLM agents are good at following instructions, but they aren't very good at learning from their own interaction with an environment.  

    Think about an agent working on a website.  
    
    For example, the user says:  "Find me a blue shirt under $20 and add it to the cart."  

    The agent might do:  

        Open website  
            ↓  
        Search shirts  
            ↓  
        Look at results  
            ↓  
        Click a shirt  
            ↓  
        Check price  
            ↓  
        Add to cart  

    The problem isn't necessarily that the LLM can't understand English.  

    The problem is:  

        - How does it learn what happens when it makes a decision?

    Suppose it clicks the wrong shirt. A human naturally learns:  

        - "That wasn't what I wanted. Next time, I'll check the price before clicking."  

    But a traditionally trained LLM doesn't necessarily get that experience during training. And this is the problem the paper is trying to attack.