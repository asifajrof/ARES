# virutal environment

- do not use python 3.11. causes dependency issues. 
- tested with 3.8.17

```bash
python -m venv venv
venv\Scripts\activate
```

# install requirements

```bash
cd rl_interaction
pip install -r requirements.txt
```

# run

```bash
cd rl_interaction
python parallel_exec.py --list_devices "Pixel2API28" --appium_ports "4723"  --android_ports "5554" --path "apps" --timer 60 --rotation --internet --emu headless --platform_version 9.0  --iterations 10 --algo SAC --timesteps 4000 --trials_per_app 3
```