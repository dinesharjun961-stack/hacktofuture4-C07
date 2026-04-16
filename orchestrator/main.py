from orchestrator.graph import build_graph

def run_simulation():
    app = build_graph()

    initial_state = {
        "current_phase": "red_attacking",
        "system_components": ["web_server", "database"],
        "vulnerabilities_found": [],
        "patches_applied": [],
        "attack_attempts": 0,
        "system_secure": False
    }

    print("🔴 Starting Red vs Blue simulation...\n")
    result = app.invoke(initial_state)

    print(f"✅ Simulation complete!")
    print(f"Attack attempts: {result['attack_attempts']}")
    print(f"Vulnerabilities found: {len(result['vulnerabilities_found'])}")
    print(f"Patches applied: {len(result['patches_applied'])}")
    print(f"System secure: {result['system_secure']}")

if __name__ == "__main__":
    run_simulation()