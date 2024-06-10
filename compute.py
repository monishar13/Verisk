import sys
import select


def ouptutValue(inp: float, threshold: int, limit: int):
    global cumulative_sum

    inp = float(inp)
    threshold = int(threshold)
    limit = int(limit)

    if inp<=threshold:
        output = 0.0
    else:
        output = inp-threshold

        if cumulative_sum + output > limit:
            output = limit - cumulative_sum

        if cumulative_sum >= limit:
            output = 0.0

    cumulative_sum += output

    return output

if __name__ == "__main__":
    threshold_value = int(sys.argv[1])
    limit_value = int(sys.argv[2])

    outputList = []
    cumulative_sum = 0

    try:
        input_count = 0
        while input_count < 100:
            print("Input (Enter E to exit): ", end="", flush=True)
            # ready, _, _ = select.select([sys.stdin], [], [], 15)
            # if ready:
            line = sys.stdin.readline().strip()
            if line:
                try:
                    input_value = float(line)
                    if input_value < 0.0 or input_value > 1_000_000_000.0:
                        raise ValueError()
                except ValueError:
                    print("Invalid input. Each line must contain a decimal value between 0.0 and 1,000,000,000.0.")
                    sys.exit(1)
                        
                output = ouptutValue(input_value, threshold_value, limit_value)
                outputList.append(output)
                print(f"Output: {output:.1f}")
            # else:
            #         break
    except Exception as e:
        print(f"Error processing input: {e}")
        sys.exit(1)
    finally:
        print(f"Cumulative Sum: {cumulative_sum:.1f}")