# latent-space-manipulation
latent-space-manipulation/
# Latent Space Manipulation

This project demonstrates how to manipulate latent vectors in the direction of a learned semantic attribute (e.g., smile, glasses).

## Usage

- `manipulate_latents.py`: Adds scaled direction vector to a latent code
- `latent_utils.py`: Learn semantic directions and interpolate between latents
- `demo.ipynb`: Example with simulated vectors

## Example
Given:
- A latent vector `w`
- A direction `d`

You can compute:
```python
w_new = w + alpha * d

