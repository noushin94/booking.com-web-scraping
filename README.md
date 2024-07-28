#  Booking.com Web Scraping Project
![image](https://github.com/user-attachments/assets/087c7596-a21d-4f1c-bdac-2d2309527198)


## Overview

This repository contains a web scraping project focused on extracting information from a Booking.com hotel page. The script parses an HTML file of a specific hotel, extracts relevant details such as hotel name, address, rating, important facilities, room types, and prices. The goal is to automate the extraction of structured data from Booking.com hotel listings for further analysis or integration into other applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How It Works](#how-it-works)


## Introduction

Web scraping is a powerful technique to collect data from web pages. This project demonstrates how to scrape a hotel listing from Booking.com using BeautifulSoup in Python. The extracted data includes the hotel's name, address, rating, important facilities, room types, and prices, which can be useful for travel-related applications, price comparisons, or data analysis.

## Features

- **Extract Hotel Information**: Scrape the hotel's name, address, and rating.
- **Retrieve Important Facilities**: Collect information about the hotel's important facilities.
- **Room Types and Prices**: Extract room types and corresponding prices.
- **Handle Missing Data**: Gracefully handle cases where certain data might be missing.
- **Structured Output**: Provide structured output in the form of lists and dictionaries for easy integration.

## How It Works

1. **Load HTML File**: Read the HTML content of a Booking.com hotel page from a local file.
2. **Parse HTML**: Use BeautifulSoup to parse the HTML content and locate the necessary elements.
3. **Extract Information**:
   - **Hotel Name, Address, and Rating**: Extract using specific HTML tags and classes.
   - **Important Facilities**: Extract facilities listed as important.
   - **Room Types and Prices**: Identify room types and their prices based on `data-block-id` attributes.
4. **Handle Missing Data**: Implement checks to handle missing or incomplete data gracefully.
5. **Output Data**: Print the extracted data in a structured format.

