# Smart Urban Ecosystem Simulation

A multi-agent system simulation modeling urban interactions between residents, energy providers, transportation, commercial entities, and environmental factors.

## Project Structure

```
mas_project/
├── agents/
│   ├── commercial.py     # Commercial agent implementation
│   ├── energy.py         # Energy provider agent
│   ├── environment.py    # Environmental monitoring agent
│   ├── resident.py       # Resident agent implementation
│   └── transport.py      # Transportation service agent
├── core/
│   ├── model.py         # Main simulation model
|
├── visualization/
│   └── server.py        # Mesa visualization server
├── reports/             # Generated simulation reports
├── run.py              # Batch simulation runner
└── README.md           # This file
```

## Features

- **Multiple Agent Types:**
  - Residents with energy needs and transport requirements
  - Energy providers managing resource distribution
  - Transport services handling movement requests
  - Commercial entities managing inventory and sales
  - Environmental monitors tracking pollution levels

- **Real-time Visualization:**
  - Interactive grid display
  - Dynamic agent state visualization
  - Live charts tracking key metrics
  - Color-coded agent states

- **Data Collection:**
  - Tracks resident energy levels
  - Monitors pollution accumulation
  - Records energy distribution
  - Logs commercial transactions

## Requirements

- Python 3.8 or higher
- Mesa framework
- Pandas (for data analysis)
- Tornado (for visualization)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mas_project.git
cd mas_project

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install mesa pandas
```

## Usage

### Running the Visual Simulation

```bash
python visualization/server.py
```
Then open your web browser and navigate to: `http://localhost:8521`

### Running Batch Simulation

```bash
python run.py
```
This will:
- Run the simulation for 100 steps
- Generate data in the reports directory
- Create a CSV file with simulation results

## Simulation Components

### Agents

1. **Resident Agent**
   - Consumes energy
   - Requests transportation
   - Makes purchases

2. **Energy Agent**
   - Distributes energy
   - Generates resources
   - Tracks distribution

3. **Transport Agent**
   - Handles movement requests
   - Generates pollution
   - Manages capacity

4. **Commercial Agent**
   - Manages inventory
   - Processes sales
   - Handles restocking

5. **Environmental Agent**
   - Monitors pollution
   - Issues warnings
   - Tracks environmental impact

### Visualization

- Grid-based display
- Color-coded agents:
  - Blue: Residents (normal energy)
  - Red: Residents (low energy)
  - Yellow: Energy provider
  - Green: Transport
  - Brown: Environmental monitor
  - Orange: Commercial entity

### Data Collection

Tracks multiple metrics:
- Number of residents with low energy
- Total pollution levels
- Energy distribution amounts
- Commercial sales volume