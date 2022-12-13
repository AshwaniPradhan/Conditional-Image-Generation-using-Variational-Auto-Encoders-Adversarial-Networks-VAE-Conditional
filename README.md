# Conditional-Image-Generation-using-Variational-Auto-Encoders-Adversarial-Networks-VAE-Conditional
We present a type of hybrid generative model that combines the strength of both Variational Auto-Encoders(VAEs) and Generative Adversarial Networks(GANs) to generate an image for the label provided by the user. 

The overview of the architecture implemented by us is shown below:

![VAE-GANs image drawio](https://user-images.githubusercontent.com/89834934/207172791-df68b5e7-bae1-48fc-8028-2248c8b599a5.png)

### Requirements

1. PyTorch, Standard Python Libraries

2. WandB account to log the outputs on an MLOPs server. You need to use wandb key to login (wandb.login(key='**your-key**')

3. GPU for faster training (if available)

## File Structure

1. Data Folder - Folder containing all the functions for dataloaders for different datasets (CIFAR, MNIST, Fashion MNIST)

2. conditional_vae-gan_code.ipynb - Code to run the cVAEGAN implementation and test its results on the different datasets

3. conditional_gan.ipynb - Conditional GAN implementation to compare the performance of our model

## Instructions to run the models

1. Import the Dataset - Run the program in the datafolder to generate the Dataloaders

2. Run each cell in ipynb to train the functions

3. Run the main training block with the selected dataset to generate the results.


