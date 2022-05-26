# Powerful Pipes Log Viewer

![License](https://img.shields.io/badge/APACHE-2-SUCCESS)

![Logo](https://raw.githubusercontent.com/42Crunch/powerful-pipes-log-viewer/main/docs/logo-250x250.png)

## Index
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Install](#install)
- [Quick start](#quick-start)
  - [Getting help](#getting-help)
  - [Listing log entries](#listing-log-entries)
    - [From a file](#from-a-file)
    - [From stdin](#from-stdin)
    - [Displaying only exceptions](#displaying-only-exceptions)
    - [Displaying minimum log level](#displaying-minimum-log-level)
    - [Streaming mode](#streaming-mode)
  - [Show entries details](#show-entries-details)
    - [From a file](#from-a-file-1)
    - [From stdin](#from-stdin-1)
    - [Displaying only exceptions](#displaying-only-exceptions-1)
    - [Displaying minimum log level](#displaying-minimum-log-level-1)
    - [Streaming mode](#streaming-mode-1)
    - [Displaying specific entry](#displaying-specific-entry)
  - [Authors](#authors)
  - [License](#license)
  - [Contributions](#contributions)
  - [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

In a nutshell ``Powerful Pipes Log Viewer`` is a command line tools for watching ``Powerful Pipes`` logs.

# Install

```bash
> pip install powerful-pipes-log-viewer 
```

# Quick start

## Getting help

```bash
> log-viewer help 
Usage: log-viewer [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  help  Displays help
  list  List long entries (default)
  show  Show log entry details
```

## Listing log entries

### From a file

```bash
>  log-viewer list logs.txt
1)   [   INFO  ] pipe-processing -> 'My log'
2)   [   ERROR ] pipe-processing -> 'Ey I\'m another log'
3)   [Exception] pipe-processing -> '__init__() missing 1 required positional argument: 'source_raw''
```

### From stdin

```bash
>  cat logs.txt | log-viewer list
1)   [   INFO  ] pipe-processing -> 'My log'
2)   [   ERROR ] pipe-processing -> 'Ey I\'m another log'
3)   [Exception] pipe-processing -> '__init__() missing 1 required positional argument: 'source_raw''
```

### Displaying only exceptions

```bash
>  cat logs.txt | log-viewer list -e
1)   [Exception] pipe-processing -> '__init__() missing 1 required positional argument: 'source_raw''
```

### Displaying minimum log level

```bash
>  cat logs.txt | log-viewer list --log-level error
1)   [   ERROR ] pipe-processing -> 'Ey I\'m another log'
2)   [Exception] pipe-processing -> '__init__() missing 1 required positional argument: 'source_raw''
```

### Streaming mode

In streaming mode all raw input data from the previous pipe will be streamed to the stdout

> log-viewer writes all the console results in stderr

```bash
>  cat logs.txt | log-viewer list --stream > stream.results.txt
1)   [   INFO  ] pipe-processing -> 'My log'
2)   [   ERROR ] pipe-processing -> 'Ey I\'m another log'
3)   [Exception] pipe-processing -> '__init__() missing 1 required positional argument: 'source_raw''
> wc stream.results.txt
3   98   5291 stream.results.txt
```

## Show entries details

### From a file

```bash
>  log-viewer show logs.txt
+--------------+------------------------------------------------------------------------------------------+
| Number       | 1                                                                                        |
+--------------+------------------------------------------------------------------------------------------+
| Command Line | pipe-processing -c 11 -A                                                                 |
+--------------+------------------------------------------------------------------------------------------+
| Date         | 2022-05-25 16:00:38.951848                                                               |
+--------------+------------------------------------------------------------------------------------------+
| Type         | INFO                                                                                     |
+--------------+------------------------------------------------------------------------------------------+
| Message      | My log                                                                                   |
+--------------+------------------------------------------------------------------------------------------+

+--------------+------------------------------------------------------------------------------------------+
| Number       | 2                                                                                        |
+--------------+------------------------------------------------------------------------------------------+
| Command Line | pipe-processing -c xxx -A                                                                |
+--------------+------------------------------------------------------------------------------------------+
| Date         | 2022-05-25 16:05:39.951848                                                               |
+--------------+------------------------------------------------------------------------------------------+
| Type         | ERROR                                                                                    |
+--------------+------------------------------------------------------------------------------------------+
| Message      | Ey I\'m another log                                                                      |
+--------------+------------------------------------------------------------------------------------------+

+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Number            | 3                                                                                                                               |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Command Line      | pipe-processing -c xxx -A                                                                                                       |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Date              | 2022-05-25 16:10:41.360994                                                                                                      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Type              | Exception                                                                                                                       |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Extra data        | {                                                                                                                               |
|                   |     "exception": "__init__() missing 1 required positional argument: 'source_raw'"                                              |
|                   | }                                                                                                                               |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Exception         | TypeError                                                                                                                       |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Exception Message | __init__() missing 1 required positional argument: 'source_raw'                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Exception file    | /Projects/demos/pipe-processing                                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Stack Trace       |   File "/Projects/demos/pipe-processing", line 430, in actor_model                                                              |
|                   |     normalized = normalize_model(info)                                                                                          |
|                   |                                                                                                                                 |
|                   |   File "/Projects/demos/pipe-processing", line 61, in actor_model_loader                                                        |
|                   |     actor = Actor(                                                                                                              |
|                   |                                                                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Exception User    | __init__() missing 1 required positional argument: 'source_raw'                                                                 |
|     Message       |                                                                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------+
```

### From stdin

Works in the same way as ``list`` command.

### Displaying only exceptions

Works in the same way as ``list`` command.

### Displaying minimum log level

Works in the same way as ``list`` command.

### Streaming mode

Works in the same way as ``list`` command.

In streaming mode all raw input data from the previous pipe will be streamed to the stdout

### Displaying specific entry

```bash
>  log-viewer show -n 2 logs.txt
+--------------+------------------------------------------------------------------------------------------+
| Number       | 2                                                                                        |
+--------------+------------------------------------------------------------------------------------------+
| Command Line | pipe-processing -c xxx -A                                                                |
+--------------+------------------------------------------------------------------------------------------+
| Date         | 2022-05-25 16:05:39.951848                                                               |
+--------------+------------------------------------------------------------------------------------------+
| Type         | ERROR                                                                                    |
+--------------+------------------------------------------------------------------------------------------+
| Message      | Ey I\'m another log                                                                      |
+--------------+------------------------------------------------------------------------------------------+
```

## Authors

Powerful Pipes was made by 42Crunch Research Team:

- `jc42 <https://github.com/jc42c>`_
- `cr0hn <https://github.com/cr0hn>`_


## License

Powerful Pipes is Open Source and available under the [Apache 2](https://github.com/42crunch/powerful-pipes-log-viewer/blob/main/LICENSE).

## Contributions

Contributions are very welcome. See [CONTRIBUTING.md](https://github.com/42crunch/powerful-pipes-log-viewer/blob/main/CONTRIBUTING.md) or skim existing tickets to see where you could help out.

Acknowledgements
----------------

Project logo thanks to [Visitor icons created by pongsakornRed - Flaticon](https://www.flaticon.com/free-icons/visitor)
