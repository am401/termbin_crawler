# Termbin Crawler
Termbin Crawler is a Python script that automates crawling [Termbin](https://termbin.com) links.

# Changelog
## 2022-02-09
### Added
- `argparse` arguments to the command line
## [ 0.0.5 ] 2021-08-21
### Added
- Checks to ensure `user_agents.txt` and the `downloads` directory exist before running the script
- Iteration counter, especially for when a high number of links are being checked

## [ 0.0.4 ] 2021-02-04
### Changed
- Text of skipping path when found in history
### Added
- `timeout=5` to the request call

## [ 0.0.4 ] 2021-01-06
### Added
- Date of scan to filename when downloading content by adding the `today` variable to `save_file()`
- Error handling if the `user_agents.txt` file is not present
- Date of the scan to the `footer()` function
- `else` statement to `__main__` logic if other than 200 or 404 HTTP resonse code is received
### Changed
- Renamed the `get_url()` function to `initiate_request()` to better fit its function

## [ 0.0.3 ] 2021-01-05
### Changed
- `get_link()` function's return value just returns r as opposed to r.status_code
### Added
- New function `save_file()` downloads the content for links that return a 200 response code

## [ 0.0.2 ] 2021-01-04
### Added
- Function to handle loading User Agents from a text file
- Better comments for functions
### Removed
- List of User Agents hard coded in to script

## [ 0.0.1 ] 2021-01-04
### Added
- Initial commit. Features include a set number iterations the script goes through and generates links
- Added color coding (green for 200 response codes and red for 404)
- Added timer to measure how long the script takes to complete
- Information within the footer at time of completion including total scans and a break down of results
