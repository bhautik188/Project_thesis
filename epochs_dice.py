import matplotlib.pyplot as plt

log_path = "/Users/bhautikposhiya/ThesProj/result/training_log_2025_6_11_16_08_52.txt"  # ← Update this path

epochs = []
dice_scores = []

with open(log_path, "r") as f:
    for line in f:
        if "train dice" in line.lower():
            parts = line.strip().split()
            for i, part in enumerate(parts):
                if "Epoch" in part:
                    epoch = int(parts[i+1])
                if "train" in part.lower() and "dice" in parts[i-1].lower():
                    try:
                        dice = float(parts[i+1])
                        epochs.append(epoch)
                        dice_scores.append(dice)
                    except:
                        pass

plt.figure(figsize=(10, 5))
plt.plot(epochs, dice_scores, color="blue", linewidth=2, label="Training Dice")
plt.xlabel("Epoch")
plt.ylabel("Dice Score")
plt.title("Training Dice Score Across Epochs")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("training_dice_score_plot.png")
plt.show()