# Changelog
## [ 0.0.3 ] 2021-01-05
### Changed
- getlink() function's return value just returns r as opposed to r.status_code
### Added
- New function save_file() downloads the content for links that return a 200 response code
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
