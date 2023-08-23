# CS420-Final-Project
This is the GitHub Repository for CS420 Final Project at UTK.

# Project Goals
- [x] Training an AI using Recurrent Neural Networks with lots of classical music, and making it **create a new classical song** based on what it learned.
- [x] Incorporate autoencoder on the recurrent neural network model.
- [ ] Incorporate another bio-inspired approach, like EA or PSO to do hyperparameter optimization on the recurrent neural network.
- [ ] To avoid overfitting, explore adding a bit of randomness or noise to inputs.

## Setup
"Final Project.py" in the Code folder uses these libraries:
* os
* mido
* numpy
* tensorflow

You can do `pip install` for `mido`, `numpy`, and `tensorflow`. We used Anaconda for using tensorflow library.
"Final Project.py" takes the input as a folder of MIDI files and output a MIDI file.
To modify input and output direction, change `data_dir` on line 7 and `midi_file.save` on line 89 respectively.

## Related Works
**Papers**
* [Composing Music With Recurrent Neural Networks](https://www.danieldjohnson.com/2015/08/03/composing-music-with-recurrent-neural-networks/)
  * [Chopin Music Generation with RNN and Deep Learning](https://www.youtube.com/watch?v=j60J1cGINX4)
  * [Their github](https://github.com/danieldjohnson/biaxial-rnn-music-composition) 
* [Automatic Music Generator Using Recurrent Neural Network](https://www.atlantis-press.com/journals/ijcis/125941516/view)
  * If the link is broken: [Automatic Music Generator Using Recurrent Neural Network.pdf](https://github.com/jkim172vols/CS420-Final-Project/files/11130249/125941516.pdf)
* [A-First-Look-at-Music-Composition-using-LSTM-Recurrent-Neural-Networks](https://people.idsia.ch/~juergen/blues/IDSIA-07-02.pdf)
* [A-Hybrid-Recurrent-Neural-Network-For-Music-Transcription](https://ieeexplore.ieee.org/abstract/document/7178333)
* [MidiNet-A-Convolutional Generative-Adversial-Network-for-Symbolic-Domain-Music-Generation](https://arxiv.org/abs/1703.10847)
* [Creating Melodies with evolving recurrent neural networks](https://ieeexplore.ieee.org/abstract/document/938515)
* [Algorithmic Composition of Melodies with Deep Recurrent Neural Networks](https://arxiv.org/pdf/1606.07251.pdf)
* [Music Composition Using Combination of Genetic Algorithms and Recurrent Neural Networks](https://ieeexplore.ieee.org/abstract/document/4626654)
* [Beat and Downbeat Tracking of Symbolic Music Data Using Deep Recurrent Neural Networks](https://ieeexplore.ieee.org/abstract/document/9306494)
* [Composing Multi-Instrumental Music with Recurrent Neural Networks](https://ieeexplore.ieee.org/abstract/document/8852430)

**Websites**
* [Music by Iteration](https://www.youtube.com/watch?v=A2gyidoFsoI)
* [Classical Piano Midi Page](http://www.piano-midi.de/)
* [Wolfram Tones](https://tones.wolfram.com/generate/GeUMZgjSdKxvvIRlCfSZG2IvIKunweXMSI17Q5idNsfphq)
* [How to Generate Music using a LSTM Neural Network in Keras](https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5)
  * [Their github](https://github.com/Skuldur/Classical-Piano-Composer)
* [Implementing Neural Networks Using TensorFlow](https://www.geeksforgeeks.org/implementing-neural-networks-using-tensorflow/)
* [TensorFlow 2 quickstart for beginners](https://www.tensorflow.org/tutorials/quickstart/beginner)
* [Autoencoder](https://www.tensorflow.org/tutorials/generative/autoencoder)
