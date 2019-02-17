#include <gtest/gtest.h>

#include <foo.h>

TEST(Foo, DefaultCase) {
  const uint32_t answer = foo();
  ASSERT_TRUE(answer);
}
