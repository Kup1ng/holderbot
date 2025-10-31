"""
Utility functions for translating English texts to Persian
"""
import re
from datetime import datetime
from typing import Optional
import jdatetime


def translate_expire_strategy(text: str) -> str:
    """
    Translate expire strategy text from English to Persian
    """
    # Extract the pattern: text (explanation)
    pattern = r"(.+?)\s*\((.+?)\)"
    match = re.match(pattern, text)
    
    if match:
        strategy_type = match.group(1).strip()
        explanation = match.group(2).strip()
        
        # Handle different strategy types
        if strategy_type == "never":
            return "بدون محدودیت"
        
        elif strategy_type == "start_on_first_use":
            # Extract days from "31 days after first use"
            days_match = re.search(r"(\d+)\s+days", explanation)
            if days_match:
                days = days_match.group(1)
                return f"{days} روز پس از اولین اتصال"
            return explanation
        
        elif strategy_type == "fixed_date":
            # Extract days from "in 19 day" or "in X days"
            days_match = re.search(r"in\s+(\d+)\s+day", explanation)
            if days_match:
                days = days_match.group(1)
                return f"{days} روز"
            return explanation
        
        elif strategy_type == "expire_on_date":
            # Extract date from explanation
            date_match = re.search(r"(\d{4}-\d{2}-\d{2})", explanation)
            if date_match:
                date_str = date_match.group(1)
                try:
                    # Convert to Jalali date
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    jalali_date = jdatetime.date.fromgregorian(date=date_obj.date())
                    return f"{jalali_date.day}-{jalali_date.month}-{jalali_date.year}"
                except Exception:
                    return date_str
            return explanation
    
    # Handle simple cases without parentheses
    if text == "unlimited":
        return "نامحدود"
    elif text == "expired":
        return "منقضی شده"
    
    return text


def translate_data_limit(text: str) -> str:
    """
    Translate data limit text from English to Persian
    """
    if not text:
        return text
    
    # Replace GB with گیگابایت
    text = re.sub(r"(\d+(?:\.\d+)?)\s*GB", r"\1 گیگابایت", text)
    
    # Replace MB with مگابایت
    text = re.sub(r"(\d+(?:\.\d+)?)\s*MB", r"\1 مگابایت", text)
    
    # Handle unlimited case
    if text.lower() == "unlimited":
        return "نامحدود"
    
    return text