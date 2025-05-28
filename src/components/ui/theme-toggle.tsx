import * as React from 'react';
import { motion } from 'framer-motion';
import { useTheme } from '@/components/providers';

const variants = {
  initial: { scale: 0.6, rotate: 90 },
  animate: { scale: 1, rotate: 0, transition: { duration: 0.3 } },
  exit: { scale: 0.6, rotate: 90 },
};

const iconVariants = {
  initial: { opacity: 0, y: -10 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: 10 },
};

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      className="fixed bottom-4 right-4 inline-flex h-12 w-12 items-center justify-center rounded-full bg-primary/10 backdrop-blur-sm transition-colors hover:bg-primary/20"
    >
      {theme === 'dark' ? (
        <motion.svg
          key="sun"
          initial="initial"
          animate="animate"
          exit="exit"
          variants={variants}
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6 text-yellow-500"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <circle cx="12" cy="12" r="5" className="fill-current" />
          <motion.path
            variants={iconVariants}
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M12 1v2m0 18v2M4.22 4.22l1.42 1.42m12.72 12.72l1.42 1.42M1 12h2m18 0h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"
          />
        </motion.svg>
      ) : (
        <motion.svg
          key="moon"
          initial="initial"
          animate="animate"
          exit="exit"
          variants={variants}
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6 text-slate-900"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <motion.path
            variants={iconVariants}
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
          />
        </motion.svg>
      )}
    </motion.button>
  );
} 