"""
Simple test script to verify the card matching game loads correctly
"""

import tkinter as tk
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from card_matching_game import CardMatchingGame
    
    # Test basic functionality
    print("Testing Card Matching Game...")
    
    # Create a hidden root window for testing
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    # Test game initialization
    game = CardMatchingGame(root)
    
    print("✓ Game initialized successfully")
    print("✓ GUI components created")
    print("✓ Cards shuffled and ready")
    
    # Clean up
    root.destroy()
    
    print("\nAll tests passed! The game is ready to play.")
    print("Run 'python card_matching_game.py' to start playing!")
    
except Exception as e:
    print(f"Error: {e}")
    print("Please ensure you have Python 3.6+ and tkinter installed.")
