# Model Checkpoints Directory

This directory stores model checkpoints during training.

## Purpose

- Save model state at each epoch
- Enable training resumption if interrupted
- Track model improvement over time
- Compare early vs late training performance

## Naming Convention

```
{model_name}_{epoch}_{val_loss}.h5
```

Example:
```
lstm_epoch_010_0.0523.h5
lstm_epoch_020_0.0412.h5
```

## Note

Checkpoints are NOT tracked in git (too large).
Only the best model is saved to `Trained_Models/`.
