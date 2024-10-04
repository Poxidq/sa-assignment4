# Team members
- Vadim Iarullin
- Aleksandr Efremov
- Nikita Sannikov
- Artur Lukianov
- Andrew Boronin

  
# Video Stream Processing with Pipes and Filters Pattern

This project implements the **Pipes and Filters** architectural pattern in Python. The application reads video frames either from a webcam or a video file and applies multiple filters (effects) in real time. Each filter is processed independently using threads, and a queue system passes frames between stages.

## Project Structure

```
.
├── filters/                 # Directory for filter-related classes
│   ├── __init__.py          
│   ├── black_white.py       
│   ├── mirror.py            
│   ├── resize.py            
│   ├── blur.py              
│   └── pipeline.py          
├── stages/                  # Directory for different pipeline stages
│   ├── __init__.py          
│   ├── video_source.py      
│   ├── display.py           
│   ├── filter_stage.py      
├── core/                    # Core pipeline logic and threading
│   ├── __init__.py          
│   ├── pipeline.py          
├── main.py                  # Main application entry point
├── Dockerfile              
├── README.md               
└── requirements.txt        

```

### Installing Dependencies

To install the required Python libraries:

```bash
pip install opencv-python
```