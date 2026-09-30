#!/usr/bin/env python3
"""Terminal pomodoro timer."""
import time, sys
def main():
      work, brk = 25*60, 5*60
      n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
      for i in range(1, n+1):
                print(f"[{i}/{n}] Fokus {work//60} menit...")
                time.sleep(work)
                print("  \a WORK DONE - istirahat 5 menit"); time.sleep(brk)
            print("Selesai semua sesi!")
if __name__ == "__main__": main()
  
