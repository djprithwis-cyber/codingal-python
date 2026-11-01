import math


FLIGHT_SECONDS = 5 * 60
SECONDS_PER_TURN = 15
STARTING_DISTANCE_KM = 14.0
STARTING_ALTITUDE_M = 1800
STARTING_SPEED_KMH = 220
RUNWAY_HEADING_ERROR = 32


def show_track(distance_km: float) -> None:
    track_length = 24
    progress = 1 - distance_km / STARTING_DISTANCE_KM
    plane_position = max(0, min(track_length - 1, round(progress * (track_length - 1))))
    track = ["-"] * track_length
    track[plane_position] = ">"
    print("  " + "".join(track) + "  DXB")


def show_status(
    distance_km: float,
    altitude_m: int,
    speed_kmh: int,
    heading_error: int,
    seconds_left: int,
) -> None:
    minutes, seconds = divmod(seconds_left, 60)
    print("\n" + "-" * 48)
    print(f"Time left: {minutes}:{seconds:02d}   Distance to Dubai: {distance_km:.1f} km")
    print(f"Altitude: {altitude_m} m   Speed: {speed_kmh} km/h")
    print(f"Runway alignment: {abs(heading_error)}° off")
    show_track(distance_km)


def get_action() -> str:
    while True:
        print("\nChoose your next action:")
        print("  A - Guided approach (descend gently, slow down, align)")
        print("  S - Slow down and descend")
        print("  T - Turn toward the runway")
        print("  H - Hold your current altitude")
        print("  Q - Quit")
        action = input("> ").strip().lower()
        if action in {"a", "s", "t", "h", "q"}:
            return action
        print("Please enter A, S, T, H, or Q.")


def move_heading_toward_runway(error: int, degrees: int) -> int:
    if error > 0:
        return max(0, error - degrees)
    return min(0, error + degrees)


def play_game() -> None:
    distance_km = STARTING_DISTANCE_KM
    altitude_m = STARTING_ALTITUDE_M
    speed_kmh = STARTING_SPEED_KMH
    heading_error = RUNWAY_HEADING_ERROR
    seconds_left = FLIGHT_SECONDS

    print("=" * 48)
    print("             DUBAI LANDING CHALLENGE")
    print("=" * 48)
    print("Arcade-style terminal game — not real flight guidance.")
    print("Land at the Dubai runway before the five-minute timer runs out.")
    print("Aim for the runway while keeping a safe in-game altitude and speed.")
    print("\nTip: Guided approach is a good starting choice.")

    while seconds_left > 0 and distance_km > 0:
        show_status(distance_km, altitude_m, speed_kmh, heading_error, seconds_left)
        action = get_action()

        if action == "q":
            print("You left the flight. Thanks for playing!")
            return
        if action == "a":
            altitude_m -= 100
            speed_kmh -= 3
            heading_error = move_heading_toward_runway(heading_error, 8)
            print("You make a gentle guided approach.")
        elif action == "s":
            altitude_m -= 100
            speed_kmh -= 12
            print("You descend gently and reduce speed.")
        elif action == "t":
            altitude_m -= 50
            speed_kmh -= 2
            heading_error = move_heading_toward_runway(heading_error, 15)
            print("You turn toward the runway.")
        else:
            speed_kmh -= 1
            print("You hold your altitude and continue toward the airport.")

        altitude_m = max(0, altitude_m)
        speed_kmh = max(0, speed_kmh)
        distance_km -= speed_kmh * SECONDS_PER_TURN / 3600
        seconds_left -= SECONDS_PER_TURN

    if distance_km > 0:
        print("\nTime is up! You did not reach the runway in time.")
        return

    print("\nThe runway is ahead!")
    if altitude_m <= 100 and 120 <= speed_kmh <= 160 and abs(heading_error) <= 5:
        print("Touchdown! You landed safely at Dubai airport. You win!")
    else:
        print("You reached the runway, but the landing conditions were not right.")
        print(f"Final altitude: {altitude_m} m")
        print(f"Final speed: {speed_kmh} km/h")
        print(f"Runway alignment: {abs(heading_error)}° off")
        print("Try again and adjust your approach.")


def main() -> None:
    while True:
        play_game()
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
