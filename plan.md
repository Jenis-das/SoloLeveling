{
  "week_number": 0,
  "start_date": "",
  "end_date": "",
  "summary": {
    "total_quests": 0,
    "completed": 0,
    "failed": 0,
    "weekly_bonus": 0,
    "weekly_penalties": 0,
    "streak_days": 0
  },
  "weekly_goals": [
    {
      "id": "",
      "title": "",
      "description": "",
      "category": "",
      "task_level": "",
      "estimated_time_min": 0,
      "base_xp": 0,
      "xp": 0,
      "stat_rewards": {
        "strength": 0,
        "agility": 0,
        "vitality": 0,
        "sense": 0,
        "intelligence": 0,
        "discipline": 0,
        "focus_stability": 0,
        "memory_retention": 0,
        "skill_mastery": 0,
        "problem_solving": 0,
        "critical_thinking": 0,
        "learning_speed": 0,
        "communication": 0,
        "english_fluency": 0,
        "time_management": 0,
        "productivity": 0,
        "confidence": 0,
        "physical_fitness": 0,
        "dynamic_skills": {
          "python": 0,
          "react": 0,
          "cpp": 0,
          "javascript": 0,
          "dsa": 0
        }
      },
      "penalty_on_fail": {
        "exp_loss": 0,
        "hp_loss": 0,
        "fatigue_gain": 0,
        "confidence": 0
      },
      "deadline": "",
      "status": "pending"
    }
  ],
  "weekly_skill_focus": {
    "primary": [],
    "secondary": []
  },
  "weekly_health_goals": {
    "steps_target": 0,
    "sleep_target_hours": 0,
    "water_intake_liters": 0
  },
  "days": {
    "monday": {
      "date": "",
      "quests": [
        {
          "id": "1",
          "title": "",
          "description": "",
          "category": "",
          "task_level": "",
          "estimated_time_min": 0,
          "base_xp": 0,
          "xp": 0,
          "stat_rewards": {
            "strength": 0,
            "agility": 0,
            "vitality": 0,
            "sense": 0,
            "intelligence": 0,
            "discipline": 0,
            "focus_stability": 0,
            "memory_retention": 0,
            "skill_mastery": 0,
            "problem_solving": 0,
            "critical_thinking": 0,
            "learning_speed": 0,
            "communication": 0,
            "english_fluency": 0,
            "time_management": 0,
            "productivity": 0,
            "confidence": 0,
            "physical_fitness": 0,
            "dynamic_skills": {
              "python": 0,
              "react": 0,
              "cpp": 0,
              "javascript": 0,
              "dsa": 0
            }
          },
          "penalty_on_fail": {
            "exp_loss": 0,
            "hp_loss": 0,
            "fatigue_gain": 0,
            "confidence": 0
          },
          "status": "pending"
        },
        {
          "id": "2",
          "title": "",
          "description": "",
          "category": "",
          "task_level": "",
          "estimated_time_min": 0,
          "base_xp": 0,
          "xp": 0,
          "stat_rewards": {
            "strength": 0,
            "agility": 0,
            "vitality": 0,
            "sense": 0,
            "intelligence": 0,
            "discipline": 0,
            "focus_stability": 0,
            "memory_retention": 0,
            "skill_mastery": 0,
            "problem_solving": 0,
            "critical_thinking": 0,
            "learning_speed": 0,
            "communication": 0,
            "english_fluency": 0,
            "time_management": 0,
            "productivity": 0,
            "confidence": 0,
            "physical_fitness": 0,
            "dynamic_skills": {
              "python": 0,
              "react": 0,
              "cpp": 0,
              "javascript": 0,
              "dsa": 0
            }
          },
          "penalty_on_fail": {
            "exp_loss": 0,
            "hp_loss": 0,
            "fatigue_gain": 0,
            "confidence": 0,
            "skill": 1
          },
          "status": "pending"
        }
      ],
      "emergency_quest": {
        "id": "",
        "title": "",
        "description": "",
        "category": "emergency",
        "task_level": "E",
        "estimated_time_min": 0,
        "base_xp": 0,
        "xp": 0,
        "stat_rewards": {},
        "penalty_on_fail": {},
        "status": "pending"
      }
    },
    "tuesday": {
      "date": "",
      "quests": [],
      "emergency_quest": null
    },
    "wednesday": {
      "date": "",
      "quests": [],
      "emergency_quest": null
    },
    "thursday": {
      "date": "",
      "quests": [],
      "emergency_quest": null
    },
    "friday": {
      "date": "",
      "quests": [],
      "emergency_quest": null
    },
    "saturday": {
      "date": "",
      "quests": [],
      "emergency_quest": null
    },
    "sunday": {
      "date": "",
      "quests": [],
      "emergency_quest": null
    }
  },
  "daily_bonus": {
    "all_tasks_completed": 0,
    "streak_multiplier": 1.0
  },
  "daily_penalties": {
    "tasks_failed": 0,
    "streak_break_penalty": 0
  },
  "config": {
    "task_levels": {
      "S": {
        "difficulty_value": 5,
        "xp_multiplier": 3.0,
        "penalty_multiplier": 2.0
      },
      "A": {
        "difficulty_value": 4,
        "xp_multiplier": 1.8,
        "penalty_multiplier": 1.5
      },
      "B": {
        "difficulty_value": 3,
        "xp_multiplier": 1.0,
        "penalty_multiplier": 1.0
      },
      "C": {
        "difficulty_value": 2,
        "xp_multiplier": 0.6,
        "penalty_multiplier": 0.5
      },
      "E": {
        "difficulty_value": 5,
        "xp_multiplier": 2.5,
        "penalty_multiplier": 0
      }
    },
    "formulas": {
      "base_xp_formula": "estimated_time_min * (difficulty_value / 10)",
      "final_xp_formula": "base_xp * xp_multiplier",
      "penalty_formula": "final_xp * 0.25 * penalty_multiplier"
    }
  }
}